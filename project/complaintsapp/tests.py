from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Complaint, ActiveIssue

class ComplaintWorkflowTests(TestCase):

    def setUp(self):
        self.client = Client()

        # Create a staff user
        self.staff_user = User.objects.create_user(username='staff', password='testpass')
        self.staff_user.is_staff = True
        self.staff_user.save()

        # Create a complaint
        self.complaint = Complaint.objects.create(
            name="John Doe",
            email="john@example.com",
            category="infrastructure",
            subcategory="potholes",
            complaint_text="There is a huge pothole on Main Street.",
            location="Main Street",
            latitude=51.501,
            longitude=-0.141
        )

    def test_staff_login(self):
        login = self.client.login(username='staff', password='testpass')
        self.assertTrue(login)

    def test_staff_dashboard_access(self):
        self.client.login(username='staff', password='testpass')
        response = self.client.get(reverse('staff_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")  # Should see complaint

    def test_verify_complaint(self):
        self.client.login(username='staff', password='testpass')
        response = self.client.get(reverse('verify_complaint', args=[self.complaint.id]))

        # Check redirect
        self.assertRedirects(response, reverse('staff_dashboard'))

        # Original complaint should be gone
        with self.assertRaises(Complaint.DoesNotExist):
            Complaint.objects.get(id=self.complaint.id)

        # ActiveIssue should exist
        active_issue = ActiveIssue.objects.get()
        self.assertEqual(active_issue.complaint.location, "Main Street")
        self.assertEqual(active_issue.verified_by, self.staff_user)

    def test_dismiss_complaint(self):
        self.client.login(username='staff', password='testpass')
        response = self.client.get(reverse('dismiss_complaint', args=[self.complaint.id]))

        # Check redirect
        self.assertRedirects(response, reverse('staff_dashboard'))

        # Complaint should be deleted
        with self.assertRaises(Complaint.DoesNotExist):
            Complaint.objects.get(id=self.complaint.id)

        # ActiveIssue should NOT exist
        self.assertEqual(ActiveIssue.objects.count(), 0)

    def test_non_staff_cannot_verify(self):
        # Create regular user
        user = User.objects.create_user(username='regular', password='testpass')
        self.client.login(username='regular', password='testpass')

        response = self.client.get(reverse('verify_complaint', args=[self.complaint.id]))
        self.assertEqual(response.status_code, 403)  # Forbidden

    def test_non_staff_cannot_access_dashboard(self):
        user = User.objects.create_user(username='regular', password='testpass')
        self.client.login(username='regular', password='testpass')

        response = self.client.get(reverse('staff_dashboard'))
        self.assertEqual(response.status_code, 403)
