from django.db import models

# Create your models here.

class SubmittedIssue(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=11)
    issue_title = models.TextField()
    issue_description = models.TextField()
    location = models.CharField(max_length=255, blank=True, null=True)  # Store location as text
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)  # Automatically store submission time 
    validated = models.BooleanField(default=False)

    def __str__(self):
        return f"Complaint by {self.name} - {self.submitted_at}"


