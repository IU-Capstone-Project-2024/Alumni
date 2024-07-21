# Generated by Django 5.0.6 on 2024-07-08 14:32

from django.db import migrations, models

def add_initial_interests(apps, schema_editor):
    Interest = apps.get_model('login', 'Interest')

    interests = [
        'Frontend', 'Backend', 'Fullstack', 'Data Science', 
        'Machine Learning', 'Artificial Intelligence', 'Cybersecurity', 'Cloud Computing', 
        'DevOps', 'Mobile Development', 'Game Development', 'UX/UI Design', 'Web Development', 
        'Open Source', 'Startups', 'IT-business', 'Networking', 'Psychology', 'Soft Skills', 
        'Career Development', 'Hackatons', 'Master Classes', 'Bar', 'Music', 'Movies',
        'Chess', 'Sports', 'Cybersports', 'Volunteering', 'Travel', 'Photography', 
        'Video Editing', 'Podcasts', 'Literature', 'Board Games', 'Cooking', 
        'Self-development', 'Personal growth', 'Health and fitness', 'Ecology', 'Social networking', 
        'Charity', 'Art', 'Running', 'Walks', 'Dancing', 'Books', 'Hiking', 'BBQ', 'CV'
    ]

    for interest in interests:
        Interest.objects.create(name=interest)

class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RunPython(add_initial_interests),
    ]
