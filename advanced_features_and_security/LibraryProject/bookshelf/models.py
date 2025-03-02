from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title
# advanced_features_and_security/users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
        
# advanced_features_and_security/users/models.py
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, date_of_birth=date_of_birth, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, date_of_birth, password, **extra_fields)
# In your other models
from django.conf import settings

class AnotherModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
# advanced_features_and_security/models.py
from django.db import models

class YourModel(models.Model):
    name = models.CharField(max_length=100)
    # Add your fields here

    class Meta:
        permissions = [
            ("can_view", "Can view the model"),
            ("can_create", "Can create the model"),
            ("can_edit", "Can edit the model"),
            ("can_delete", "Can delete the model"),
        ]
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import YourModel

content_type = ContentType.objects.get_for_model(YourModel)

permissions = {
    'can_view': Permission.objects.get(codename='can_view', content_type=content_type),
    'can_create': Permission.objects.get(codename='can_create', content_type=content_type),
    'can_edit': Permission.objects.get(codename='can_edit', content_type=content_type),
    'can_delete': Permission.objects.get(codename='can_delete', content_type=content_type),
}

groups = {
    'Editors': ['can_edit', 'can_create'],
    'Viewers': ['can_view'],
    'Admins': ['can_view', 'can_create', 'can_edit', 'can_delete'],
}

for group_name, perms in groups.items():
    group, created = Group.objects.get_or_create(name=group_name)
    for perm in perms:
        group.permissions.add(permissions[perm])
