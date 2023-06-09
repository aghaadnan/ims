# Generated by Django 3.2.18 on 2023-03-28 22:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0001_initial'),
        ('vehicles', '0002_alter_vehicle_color'),
        ('inventory', '0005_sim'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackerInstallation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('installed_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracker_installations', to='companies.company')),
                ('installed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracker_installations', to=settings.AUTH_USER_MODEL)),
                ('sim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.sim')),
                ('tracker_device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.trackerdevice')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracker_installations', to='vehicles.vehicle')),
            ],
        ),
    ]
