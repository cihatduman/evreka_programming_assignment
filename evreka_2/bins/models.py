from django.db import models


# Create your models here.
class Bin(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return "{}\t{}".format(self.latitude, self.longitude)


class Operation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BinOperation(models.Model):
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    operation_frequency = models.IntegerField()
    last_operation = models.DateTimeField()

    def __str__(self):
        return "{}\t{}\t{}\t{}".format(str(self.operation), self.bin.id, self.operation_frequency, self.last_operation)
