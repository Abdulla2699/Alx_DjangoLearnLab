from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
from django.contrib.auth import views as auth_views
from django.urls import path, include

# Login view
class CustomLoginView(auth_views.LoginView):
    template_name = 'relationship_app/login.html'

# Logout view
class CustomLogoutView(auth_views.LogoutView):
    template_name = 'relationship_app/logout.html'

# Registration view - we'll need to create a custom form for this
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')
