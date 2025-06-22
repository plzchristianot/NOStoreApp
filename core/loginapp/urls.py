from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('dashboard_admin/', views.dashboard_admin, name='dashboard_admin'),
    path('signup/', views.signup, name='signup'),
]
