from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('submit_complaint/', views.submit_complaint, name='submit_complaint'),
]

