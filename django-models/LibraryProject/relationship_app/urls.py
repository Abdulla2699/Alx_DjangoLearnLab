# In relationship_app/urls.py

from django.urls import path
from .views import register_view, login_view, logout_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
["views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name="]
["relationship_app/register.html"]
