from django.db import models
from django.utils import timezone

# Create your models here.

# models.Model significa que Post es un modelo de Django, 
# así Django sabe que debe guardarlo en la base de datos
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # Funcion para publicar post
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title