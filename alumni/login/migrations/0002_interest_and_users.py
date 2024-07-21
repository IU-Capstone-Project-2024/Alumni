# Generated by Django 5.0.6 on 2024-07-15 09:36

from django.db import migrations, models
from login.models import CustomUser

def create_custom_users(apps, schema_editor):
    
    users_data = [
        {
            "email": "alumni@innopolis.com",
            "first_name": "Alumni",
            "last_name": "Test",
            "password": "alumnitestpass"
        },
        {
            "email": "user1@example.com",
            "first_name": "User",
            "last_name": "One",
            "password": "password1"
        },
        {
            "email": "user2@example.com",
            "first_name": "User",
            "last_name": "Two",
            "password": "password2"
        },
        {
            "email": "user3@example.com",
            "first_name": "User",
            "last_name": "Three",
            "password": "password3"
        },
        {
            "email": "user4@example.com",
            "first_name": "User",
            "last_name": "Four",
            "password": "password4"
        },
        {
            "email": "user5@example.com",
            "first_name": "User",
            "last_name": "Five",
            "password": "password5"
        },
        
    ]

    for user_data in users_data:
        user = CustomUser.objects.create_user(
            email=user_data["email"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            password=user_data["password"]
        )
        user.save()
        

    '''
    superuser = CustomUser.objects.create_superuser(email=,
            first_name=,
            last_name=,
            password=)
    superuser.save()
    '''


def add_initial_interests(apps, schema_editor):
    Interest = apps.get_model('login', 'Interest')

    interests = [
        'Running', 'Walks', 'Dancing', 'Books', 'Hiking', 'BBQ', 'CV',
        'Frontend', 'Backend', 'Fullstack', 'Data Science', 
        'Machine Learning', 'Artificial Intelligence', 'Cybersecurity', 'Cloud Computing', 
        'DevOps', 'Mobile Development', 'Game Development', 'UX/UI Design', 'Web Development', 
        'Open Source', 'Startups', 'IT-business', 'Networking', 'Psychology', 'Soft Skills', 
        'Career Development', 'Hackathons', 'Master Classes', 'Bar', 'Music', 'Movies', 
        'Chess', 'Sports', 'Cybersports', 'Volunteering', 'Travel', 'Photography', 
        'Video Editing', 'Podcasts', 'Literature', 'Board Games', 'Cooking', 
        'Self-development', 'Personal growth', 'Health and fitness', 'Ecology', 'Social networking', 
        'Charity', 'Art'
    ]

    for interest in interests:
        Interest.objects.create(name=interest)

class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_custom_users),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RunPython(add_initial_interests),
        
    ]
