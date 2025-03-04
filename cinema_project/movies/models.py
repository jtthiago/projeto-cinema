from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255)
    duration = models.PositiveBigIntegerField(help_text="Duração em minutos")
    genre = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return self.title
    
    