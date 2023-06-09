# Generated by Django 3.2.18 on 2023-04-23 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_userprofile_is_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContactNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_numbers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
