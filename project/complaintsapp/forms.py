from django import forms
from .models import SubmittedIssue
from django.contrib.auth.forms import AuthenticationForm

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = SubmittedIssue
        fields = ['name', 'email','telephone','category','subcategory','issue_description','location', 'latitude', 'longitude']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'category': forms.Select(attrs={'class': 'form-select', 'id': 'category'}),
            'subcategory': forms.Select(attrs={'class': 'form-select', 'id': 'subcategory'}),
            'issue_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe your complaint'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'placeholder': 'Click map to set location'}),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }

class StaffLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))