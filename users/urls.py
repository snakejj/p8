from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "users"

urlpatterns = [
    path('login/', views.login, name='login'),
    path('accounts/profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),

]
