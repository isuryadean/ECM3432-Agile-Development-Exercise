from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('submit_complaint/', views.submit_complaint, name='submit_complaint'),
    path("staff/login/", views.staff_login, name="staff_login"),
    path("staff/logout/", views.staff_logout, name="staff_logout"),
    path("staff/dashboard/", views.staff_dashboard, name="staff_dashboard"),
    path("staff/verify/<int:complaint_id>/", views.verify_complaint, name="verify_complaint"),
    path("staff/dismiss/<int:complaint_id>/", views.dismiss_complaint, name="dismiss_complaint"),
]

