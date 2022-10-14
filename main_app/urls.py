from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('accounts/chef/', views.RegisterChef.as_view(), name="register_chef"),
    path('accounts/client/', views.RegisterClient.as_view(), name="register_client"),
    path('accounts/profile/', views.Profile.as_view(), name="profile"),
    path('chefs/', views.ChefsList.as_view(), name="chefs_list"),
    path('chefs/<int:pk>/', views.ChefDetail.as_view(), name="chef_detail"),
    path('chefs/<int:pk>/request', views.RequestCreate.as_view(), name="request_create"),
    path('requests/<int:pk>/update',views.RequestUpdate.as_view(), name="request_update"),
    path('requests/<int:pk>/delete',views.RequestDelete.as_view(), name="request_delete"),
    path('chefs/<int:pk>/comment', views.CommentCreate.as_view(), name="comment_create"),
]