from authapp.views import *
from django.urls import path

urlpatterns = [

    path('index', index),
    path('person', people)
]
