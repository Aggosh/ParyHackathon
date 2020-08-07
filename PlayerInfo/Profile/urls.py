from django.urls import path, include
from .views import profile

urlpatterns = [path("<str:nickname>/", profile)]
