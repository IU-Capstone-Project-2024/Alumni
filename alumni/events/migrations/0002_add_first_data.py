from django.db import migrations
from django.utils import timezone

def add_first_data(apps, schema_editor):
    Events = apps.get_model('events', 'Events')
    Interest = apps.get_model('login', 'Interest')

    requests = [
        {
            'event_name': 'Tech Conference 2024',
            'author_email': 'john.doe@innopolis.university',
            'author_name': 'John',
            'author_surname': 'Doe',
            'author_alias': '@johndoe',
            'country': 'Russia',
            'city': 'Innopolis',
            'address': '123 Innopolis Street',
            'date': timezone.now() + timezone.timedelta(days=20),
            'description': 'Annual tech conference with leading experts in the industry.',
            'tags': ['IT-business', 'Networking', 'Career Development']
        },
        {
            'event_name': 'AI Summit 2024',
            'author_email': 'jane.smith@innopolis.university',
            'author_name': 'Jane',
            'author_surname': 'Smith',
            'author_alias': '@janesmith',
            'country': 'Russia',
            'city': 'Moscow',
            'address': '456 Moscow Street',
            'date': timezone.now() + timezone.timedelta(days=25),
            'description': 'Gathering of AI professionals and enthusiasts.',
            'tags': ['Artificial Intelligence', 'Machine Learning', 'IT-business']
        },
        {
            'event_name': 'Startup Pitch Day',
            'author_email': 'mike.brown@innopolis.university',
            'author_name': 'Mike',
            'author_surname': 'Brown',
            'author_alias': '@mikebrown',
            'country': 'Russia',
            'city': 'St. Petersburg',
            'address': '789 St. Petersburg Street',
            'date': timezone.now() + timezone.timedelta(days=30),
            'description': 'Event where startups present their ideas to investors.',
            'tags': ['Startups', 'DevOps', 'Networking']
        },
        {
            'event_name': 'Data Science Workshop',
            'author_email': 'sarah.lee@innopolis.university',
            'author_name': 'Sarah',
            'author_surname': 'Lee',
            'author_alias': '@sarahlee',
            'country': 'Russia',
            'city': 'Innopolis',
            'address': '101 Innopolis Street',
            'date': timezone.now() + timezone.timedelta(days=35),
            'description': 'Hands-on workshop on data science techniques.',
            'tags': ['Data Science', 'Machine Learning']
        },
        {
            'event_name': 'Art Exhibition',
            'author_email': 'alex.green@innopolis.university',
            'author_name': 'Alex',
            'author_surname': 'Green',
            'author_alias': '@alexgreen',
            'country': 'France',
            'city': 'Paris',
            'address': '202 Paris Street',
            'date': timezone.now() + timezone.timedelta(days=40),
            'description': 'Exhibition featuring contemporary art pieces.',
            'tags': ['Art']
        },
        {
            'event_name': 'Music Festival',
            'author_email': 'emma.wilson@innopolis.university',
            'author_name': 'Emma',
            'author_surname': 'Wilson',
            'author_alias': '@emmawilson',
            'country': 'UK',
            'city': 'London',
            'address': '303 London Street',
            'date': timezone.now() + timezone.timedelta(days=45),
            'description': 'Annual music festival with live performances.',
            'tags': ['Music']
        },
        {
            'event_name': 'Film Festival',
            'author_email': 'liam.thomas@innopolis.university',
            'author_name': 'Liam',
            'author_surname': 'Thomas',
            'author_alias': '@liamthomas',
            'country': 'Canada',
            'city': 'Toronto',
            'address': '404 Toronto Street',
            'date': timezone.now() + timezone.timedelta(days=50),
            'description': 'Showcasing independent films from around the world.',
            'tags': ['Movies']
        },
        {
            'event_name': 'Science Conference',
            'author_email': 'olivia.jones@innopolis.university',
            'author_name': 'Olivia',
            'author_surname': 'Jones',
            'author_alias': '@oliviajones',
            'country': 'Australia',
            'city': 'Sydney',
            'address': '505 Sydney Street',
            'date': timezone.now() + timezone.timedelta(days=55),
            'description': 'Conference discussing latest scientific discoveries.',
            'tags': ['Personal growth']
        },
        {
            'event_name': 'Fashion Show',
            'author_email': 'sophia.martin@innopolis.university',
            'author_name': 'Sophia',
            'author_surname': 'Martin',
            'author_alias': '@sophiamartin',
            'country': 'Spain',
            'city': 'Madrid',
            'address': '606 Madrid Street',
            'date': timezone.now() + timezone.timedelta(days=60),
            'description': 'Showcasing latest fashion trends.',
            'tags': ['Art', 'Social networking']
        },
        {
            'event_name': 'Gaming Expo',
            'author_email': 'james.wright@innopolis.university',
            'author_name': 'James',
            'author_surname': 'Wright',
            'author_alias': '@jameswright',
            'country': 'Japan',
            'city': 'Tokyo',
            'address': '707 Tokyo Street',
            'date': timezone.now() + timezone.timedelta(days=65),
            'description': 'Expo featuring the latest in gaming technology.',
            'tags': ['Cybersports']
        },
        {
            'event_name': 'Food and Wine Festival',
            'author_email': 'lily.white@innopolis.university',
            'author_name': 'Lily',
            'author_surname': 'White',
            'author_alias': '@lilywhite',
            'country': 'Italy',
            'city': 'Rome',
            'address': '808 Rome Street',
            'date': timezone.now() + timezone.timedelta(days=70),
            'description': 'Festival celebrating food and wine.',
            'tags': ['Alcohol', 'Social networking']
        },
    ]

    for request_data in requests:
        tags_data = request_data.pop('tags', [])

        tags = []
        for tag_name in tags_data:
            tag_obj = Interest.objects.get(name=tag_name)
            tags.append(tag_obj)

        event_obj = Events.objects.create(**request_data)
        event_obj.tags.add(*tags)

class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_first_data),
    ]
