from django.db import models


class Vehicle(models.Model):
    plate = models.CharField(max_length=100)


class NavigationRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return "{}\t{}\t{}\t{}".format(str(self.vehicle.plate), self.datetime, self.latitude, self.longitude)
