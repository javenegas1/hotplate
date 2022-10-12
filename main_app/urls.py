from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('accounts/chef/', views.RegisterChef.as_view(), name="register_chef"),
    path('accounts/client/', views.RegisterClient.as_view(), name="register_client"),
    path('accounts/profile/', views.Profile.as_view(), name="profile"),

]