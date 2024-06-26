# Generated by Django 5.0.4 on 2024-05-27 15:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_doctorappointment_appointment_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.branch'),
        ),
    ]
