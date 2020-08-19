from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.home, name='home'),
    path('mentions_legales/', views.legal_notice, name='legal_notice'),
]
