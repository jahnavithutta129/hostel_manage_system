# Generated by Django 5.0.6 on 2024-05-16 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_profile_user_facultyprofile_studentprofile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]