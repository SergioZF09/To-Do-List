from django.db import models

# Create your models here.

class PostList(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.TextField()

    def __str__(self):
        return self.title