# Generated by Django 3.2.18 on 2023-03-27 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='Color',
            field=models.CharField(max_length=255),
        ),
    ]
