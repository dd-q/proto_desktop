from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:id>/', views.home, name='home'),
]