from django import forms
from .models import SubmittedIssue

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = SubmittedIssue
        fields = ['name', 'email','telephone','issue_title','issue_description','location', 'latitude', 'longitude']
