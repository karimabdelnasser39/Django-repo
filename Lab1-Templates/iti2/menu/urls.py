from django.urls import path
from . import views

urlpatterns = [
    # This maps 127.0.0.1:8000/kitchen/ to your menu_list view
    path('', views.menu_list, name='menu_list'),
]