from django.contrib import admin
from.models import SubmittedIssue, ActiveIssue

# Register your models here.

admin.site.register(SubmittedIssue)

admin.site.register(ActiveIssue)