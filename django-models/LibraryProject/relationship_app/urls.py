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
from django.urls import path
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]
