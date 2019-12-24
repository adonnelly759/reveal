from django.urls import path
from . import views
from django.conf import settings


app_name = "reveal"
urlpatterns = [
    path('', views.index, name='index'),
]