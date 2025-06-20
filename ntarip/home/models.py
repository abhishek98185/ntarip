from django.db import models

# Create your models here.
class Contact(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    message = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.username} - {self.email}'