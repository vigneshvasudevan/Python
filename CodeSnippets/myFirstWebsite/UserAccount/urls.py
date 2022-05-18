from django.contrib import admin
from django.urls import path
from UserAccount import views
from django.views.generic import TemplateView

app_name = "UserAccount"
urlpatterns = [
    path('register/', views.register_request),
    path('login/', views.login_request, name='login'),
    path("logout", views.logout_request, name="logout"),
]