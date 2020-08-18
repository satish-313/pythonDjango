from django.db import models

# Create your models here.
class airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} : {self.code}"

class Flights(models.Model):
    origin = models.ForeignKey(airport, on_delete=models.CASCADE, related_name= "depature")
    destination = models.ForeignKey(airport, on_delete=models.CASCADE , related_name= "arrival")
    duration = models.IntegerField()

    def __str__ (self):
        return f"{self.id} : {self.origin} to {self.destination} : {self.duration}"

class passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flights , blank=True , related_name= "passengers")

    def __str__ (self):
        return f"{self.first} {self.last}"