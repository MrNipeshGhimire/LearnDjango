from django.urls import path
from .views.main_view import home

urlpatterns = [
 path("/",home)
]