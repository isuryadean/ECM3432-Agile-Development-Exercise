from django.shortcuts import render, HttpResponse
from .models import SubmittedIssue
from .forms import ComplaintForm
import json

# Create your views here.

def home(request):
    return render(request, "form.html")

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