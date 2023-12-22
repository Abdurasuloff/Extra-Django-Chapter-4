# Generated by Django 4.2.7 on 2023-11-27 21:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=250)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2023, 11, 28, 2, 5, 43, 109691))),
                ('sent', models.BooleanField(default=False)),
            ],
        ),
    ]