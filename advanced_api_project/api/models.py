from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)  # Author's name

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)  # Book's title
    publication_year = models.IntegerField()  # Year of publication
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)  # Relationship to Author

    def __str__(self):
        return self.title
