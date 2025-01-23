from django.urls import path
from . import views

urlpatterns = [
    path('complaints/', views.complaints, name='complaints'),
]
