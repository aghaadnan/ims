# Generated by Django 3.2.18 on 2023-04-03 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_sim'),
    ]

    operations = [
        migrations.AddField(
            model_name='sim',
            name='isUsed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='trackerdevice',
            name='isUsed',
            field=models.BooleanField(default=False),
        ),
    ]
