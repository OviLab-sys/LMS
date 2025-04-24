from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200, unique=True)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.id}: {self.title}"