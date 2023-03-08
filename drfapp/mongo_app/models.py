from django.db import models


class Mappack(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    ecu = models.CharField(max_length=255)
    softwareversion = models.CharField(max_length=255)
    file = models.FileField(upload_to='mappacks/')
