
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    path('',views.home, nome='home'),
]


