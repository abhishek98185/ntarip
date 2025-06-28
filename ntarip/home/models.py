from django.db import models
from django.contrib.auth.models import User

# Creating Contact
class Contact(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    message = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.username} - {self.email}'
# Creating Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='users_images/', blank=True, null=True)
    user_class = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} - {self.user_class}'