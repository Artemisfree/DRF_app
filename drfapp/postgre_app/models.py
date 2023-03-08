from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    dongle_serial = models.CharField(max_length=255)
    dongle_uuid = models.CharField(max_length=255)

    def __str__(self):
        return self.username
