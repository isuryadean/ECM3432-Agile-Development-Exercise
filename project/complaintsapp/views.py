from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import StaffLoginForm
from .models import SubmittedIssue, ActiveIssue
from .forms import ComplaintForm
import json

# Create your views here.

def home(request):
    return render(request, "home.html")

def submit_complaint(request):
    success = False

    subcategories_json = json.dumps(SubmittedIssue.SUBCATEGORY_CHOICES)

    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = ComplaintForm()
            print("✅ Complaint successfully saved!")
        else:
            print("❌ Form errors:", form.errors)  # ✅ Debugging: Print errors if form is invalid
    else:
        form = ComplaintForm()

    return render(request, 'form.html', {
        'form': form, 
        'success': success,
        'subcategories': subcategories_json,
        })

# Ensure only staff can log in
def staff_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect("staff_dashboard")  # Redirect if already logged in

    if request.method == "POST":
        form = StaffLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_staff:  # Ensure only staff can log in
                login(request, user)
                return redirect("staff_dashboard")  # Redirect to dashboard
            else:
                form.add_error(None, "You do not have staff access.")
    else:
        form = StaffLoginForm()

    return render(request, "staff_login.html", {"form": form})

# Logout staff
def staff_logout(request):
    logout(request)
    return redirect("staff_login")  # Redirect to login page

# Check if the user is a staff member
def is_staff(user):
    return user.is_staff

# Staff dashboard to review complaints
@login_required
@user_passes_test(is_staff)
def staff_dashboard(request):
    complaints = SubmittedIssue.objects.all().order_by("-submitted_at")  # Fetch complaints
    return render(request, "staff_dashboard.html", {"complaints": complaints})

@login_required
@user_passes_test(is_staff)
def verify_complaint(request, complaint_id):
    complaint = get_object_or_404(SubmittedIssue, id=complaint_id)

    # Move complaint to ActiveIssue
    ActiveIssue.objects.create(complaint=complaint, verified_by=request.user)

    # Delete from original complaints
    complaint.delete()

    return redirect("staff_dashboard")

@login_required
@user_passes_test(is_staff)
def dismiss_complaint(request, complaint_id):
    complaint = get_object_or_404(SubmittedIssue, id=complaint_id)
    complaint.delete()  # Remove complaint permanently
    return redirect("staff_dashboard")