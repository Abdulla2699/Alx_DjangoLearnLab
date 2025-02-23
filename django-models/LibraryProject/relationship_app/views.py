from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView  # Import for class-based list view
from .models import Book, Library

# Class-based view to list all books
class BookListView(ListView):
    model = Book
    template_name = 'relationship_app/list_books.html'
    context_object_name = 'books'

# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
