from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('', views.index, name='index'),
    path('dashboard_admin/', views.dashboard_admin, name='dashboard_admin'),
]
