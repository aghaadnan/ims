# Generated by Django 3.2.18 on 2023-04-04 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_auto_20230404_2249'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackerDeviceVendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='trackerdevice',
            name='vendor',
        ),
        migrations.CreateModel(
            name='TrackerDeviceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_number', models.CharField(max_length=255)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trackerdevice_vendor', to='inventory.trackerdevicevendor')),
            ],
        ),
        migrations.AlterField(
            model_name='trackerdevice',
            name='model_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trackerdevice_items', to='inventory.trackerdevicemodel'),
        ),
    ]
