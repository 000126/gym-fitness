from django.urls import path
from authapp import views

urlpatterns = [
    path('', views.home),
    path('signup', views.signup, name="signup"),
    path('login', views.handlelogin, name="login"),
    path('logout', views.handleLogout, name="logout "),
    path('contact', views.contact, name="contact"),
    path('enroll', views.enroll, name="enroll"),
    path('profile', views.profile, name="profile"),
    path('gallery', views. gallery, name="gallary"),
    path('attendance', views.attendance, name="attendance"),
    path('about', views.about, name="about"),
    path('services', views.service, name="services"),
]
