from django.urls import path
from . import views

app_name = "favorites"

urlpatterns = [
    path('favorites/', views.favorites, name='favorites'),
]
