from django.db import models


class CsvData(models.Model):
    data = models.TextField()
