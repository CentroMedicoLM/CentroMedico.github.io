from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('comunidad/', views.comunidad, name='comunidad'),
    path('revista/', views.revista, name='revista'),
    path('calendario/', views.calendario, name='calendario'),
    path('reportes/', views.reportes, name='reportes'),
]