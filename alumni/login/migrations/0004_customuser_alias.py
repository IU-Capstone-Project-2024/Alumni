# Generated by Django 5.0.6 on 2024-07-11 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_interest_remove_customuser_interests_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='alias',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]