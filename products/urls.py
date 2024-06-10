from django.urls import path
from . import views

#URLConfigurations
urlpatterns = [
    path('', views.say_hello)
]