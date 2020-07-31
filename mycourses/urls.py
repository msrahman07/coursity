from django.urls import path
from . import views

app_name = 'mycourses'

urlpatterns = [
    path('', views.index, name='index')
]