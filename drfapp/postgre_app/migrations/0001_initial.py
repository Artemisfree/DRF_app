# Generated by Django 4.1.7 on 2023-03-12 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('dongle_serial', models.CharField(max_length=255)),
                ('dongle_uuid', models.CharField(max_length=255)),
            ],
        ),
    ]
