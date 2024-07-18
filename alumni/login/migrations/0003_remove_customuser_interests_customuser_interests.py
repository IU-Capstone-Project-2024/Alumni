# Generated by Django 5.0.6 on 2024-07-15 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_interest_and_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='interests',
        ),
        migrations.AddField(
            model_name='customuser',
            name='interests',
            field=models.ManyToManyField(blank=True, to='login.interest'),
        ),
    ]