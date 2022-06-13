from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Guest(models.Model):
    guest_name = models.CharField(max_length=200)
    guest_email = models.EmailField()
    guest_occupation = models.CharField(max_length=200)
    number_of_nights = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    room_number = models.IntegerField(unique=True)
    amount = models.IntegerField()
    

    def __str__(self):
        return f'Guest {self.guest_name} in room {self.room_number}'

    
