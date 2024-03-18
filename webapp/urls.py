from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name='register'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('create_record/', views.create_record, name='create_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path("delete_record/<int:pk>", views.delete_record, name="delete_record"),
    path('record/<int:pk>', views.singular_record, name='record')
]
