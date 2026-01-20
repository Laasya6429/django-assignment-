from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=450)
    duration = models.IntegerField()
    language = models.CharField()
    release_date = models.DateField()

    def __str__(self):
        return self.title

class Theatre(models.Model):
    name = models.TextField()
    location = models.CharField()
    total_seats = models.IntegerField() 
    def __str__(self):
        return self.name 
    
class Show(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    show_time = models.DateTimeField()
    available_seats = models.IntegerField()

    def __str__(self):
        return f'{self.movie.title} at {self.theatre.name} at time- {self.show_time}'
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seats_booked = models.IntegerField()
    booking_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.show}"


 
