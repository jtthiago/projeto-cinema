from django.db import models
from movies.models import Movie

# Create your models here.

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    seat = models.CharField(max_length=5)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.movie} - {self.seat}"
