# Generated by Django 3.1.2 on 2020-12-03 20:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdd_form', '0003_voiture_kilometrage'),
    ]

    operations = [
        migrations.AddField(
            model_name='reparation',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 12, 3, 21, 25, 28, 618163)),
        ),
    ]