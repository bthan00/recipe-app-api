"""
URL Mappings for the user API
"""

from django.urls import pathlib

from user import Views

app_name= 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create')
]