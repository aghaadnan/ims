# Generated by Django 3.2.18 on 2023-03-26 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20230326_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_agent',
            field=models.BooleanField(default=False),
        ),
    ]
