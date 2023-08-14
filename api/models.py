from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create a form view to Add Class
class Class(models.Model):
    class_name = models.CharField(max_length=100)

    def __str__(self):
        return self.class_name


# Register Student and select class from dropdown
class Student(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    date_of_birth = models.DateField()
    status = models.BooleanField(default=False)
    image = models.ImageField(upload_to="profile_images/", blank=True, null=True)
    class_selected = models.ForeignKey(Class,on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.username


# Custom User Model for Student with API Token
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15,unique=True)