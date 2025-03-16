from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Author, Book

class BookAPITests(APITestCase):
    
    def setUp(self):
        # Create initial data for testing
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(
            title="Test Book", publication_year=2022, author=self.author
        )
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", kwargs={"pk": self.book.id})

    def test_get_books(self):
        # Test retrieving all books
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Should only return 1 book

    def test_get_book_detail(self):
        # Test retrieving a specific book by ID
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Book")

    def test_create_book(self):
        # Test creating a new book
        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author.id,
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        # Test updating an existing book
        data = {"title": "Updated Title", "publication_year": 2021}
        response = self.client.put(self.detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_delete_book(self):
        # Test deleting a book
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url + "?title=Test Book")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    def test_unauthenticated_access(self):
        self.client.logout()  # Simulate unauthenticated access
        response = self.client.post(self.list_url, {})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
["self.client.login"]
