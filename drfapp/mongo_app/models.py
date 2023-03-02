from django.db import models


class Mappack(models.Model):
    name = models.CharField(max_length=255)
    csv_file = models.FileField(
        upload_to='mappacks/csv', null=True, blank=True
        )
    json_file = models.FileField(
        upload_to='mappacks/json', null=True, blank=True
        )
    a2l_file = models.FileField(
        upload_to='mappacks/a2l', null=True, blank=True
        )
    kp_file = models.FileField(
        upload_to='mappacks/kp', null=True, blank=True
        )

    def __str__(self):
        return self.name
