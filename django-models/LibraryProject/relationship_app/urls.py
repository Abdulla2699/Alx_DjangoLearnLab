from django.urls import path
from .views import BookListView, add_book, edit_book, delete_book

urlpatterns = [
    path('books/', BookListView.as_view(), name='list_books'),
    path('books/add/', add_book, name="add_book"),
    path('books/edit/<int:pk>/', edit_book, name="edit_book"),
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),
]
