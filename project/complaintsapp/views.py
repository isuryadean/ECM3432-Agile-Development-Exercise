from django.shortcuts import render, HttpResponse
from .models import SubmittedIssue
from .forms import ComplaintForm

# Create your views here.

def home(request):
    return render(request, "form.html")

def submit_complaint(request):
    success = False

    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = ComplaintForm()

    return render(request, 'form.html', {'form': form, 'success': success})