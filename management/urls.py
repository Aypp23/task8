from django.urls import path
from . import views


urlpatterns = [
    path('', views.ManagementPage, name='management')
]