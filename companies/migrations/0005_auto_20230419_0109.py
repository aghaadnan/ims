# Generated by Django 3.2.18 on 2023-04-18 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_company_renew_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='is_expired',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('email_date', models.DateField()),
                ('days_before_expiry', models.PositiveIntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_templates', to='companies.company')),
            ],
        ),
    ]
