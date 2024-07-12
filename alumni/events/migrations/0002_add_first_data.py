from django.db import migrations
from django.utils import timezone

def add_first_data(apps, schema_editor):
    Events = apps.get_model('events', 'Events')

    requests = [
        {
            'event_name': 'Tech Conference 2024',
            'author_email': 'john.doe@innopolis.university',
            'author_name': 'John',
            'author_surname': 'Doe',
            'author_alias': '@johndoe',
            'country': 'USA',
            'city': 'San Francisco',
            'address': '123 Market Street',
            'date': timezone.now() + timezone.timedelta(days=20),
            'description': 'Annual tech conference with leading experts in the industry.',
            'tags': ['IT-business', 'Networking', 'Career Development']
        },
        {
            'event_name': 'Art Expo 2024',
            'author_email': 'jane.smith@innopolis.university',
            'author_name': 'Jane',
            'author_surname': 'Smith',
            'author_alias': '@janesmith',
            'country': 'France',
            'city': 'Paris',
            'address': '456 Rue de Rivoli',
            'date': timezone.now() + timezone.timedelta(days=20),
            'description': 'Showcase of contemporary art from around the world.',
            'tags': ['Art', 'Exhibition']
        },
        {
            'event_name': 'Music Festival 2024',
            'author_email': 'mike.brown@example.com',
            'author_name': 'Mike',
            'author_surname': 'Brown',
            'author_alias': '@mikebrown',
            'country': 'UK',
            'city': 'London',
            'address': '789 Kings Road',
            'date': timezone.now() + timezone.timedelta(days=30),
            'description': 'A weekend of live music performances from top artists.',
            'tags': ['Music', 'Festival']
        },
        {
            'event_name': 'Food and Wine Fair',
            'author_email': 'sarah.lee@example.com',
            'author_name': 'Sarah',
            'author_surname': 'Lee',
            'author_alias': '@sarahlee',
            'country': 'Italy',
            'city': 'Rome',
            'address': '101 Via Veneto',
            'date': timezone.now() + timezone.timedelta(days=40),
            'description': 'Discover the best food and wine from Italy.',
            'tags': ['food', 'wine', 'fair']
        },
        {
            'event_name': 'Book Fair 2024',
            'author_email': 'alex.green@example.com',
            'author_name': 'Alex',
            'author_surname': 'Green',
            'author_alias': '@alexgreen',
            'country': 'Germany',
            'city': 'Berlin',
            'address': '202 Alexanderplatz',
            'date': timezone.now() + timezone.timedelta(days=50),
            'description': 'Annual book fair with authors from around the world.',
            'tags': ['books', 'fair', '2024']
        },
        {
            'event_name': 'Film Festival 2024',
            'author_email': 'emma.wilson@example.com',
            'author_name': 'Emma',
            'author_surname': 'Wilson',
            'author_alias': '@emmawilson',
            'country': 'Canada',
            'city': 'Toronto',
            'address': '303 Queen Street',
            'date': timezone.now() + timezone.timedelta(days=60),
            'description': 'Showcasing the latest in independent film.',
            'tags': ['film', 'festival', '2024']
        },
        {
            'event_name': 'Science Symposium',
            'author_email': 'liam.thomas@example.com',
            'author_name': 'Liam',
            'author_surname': 'Thomas',
            'author_alias': 'liamthomas',
            'country': 'Australia',
            'city': 'Sydney',
            'address': '404 George Street',
            'date': timezone.now() + timezone.timedelta(days=70),
            'description': 'Leading scientists discuss the latest discoveries.',
            'tags': ['science', 'symposium']
        },
        {
            'event_name': 'Startup Pitch Night',
            'author_email': 'olivia.jones@example.com',
            'author_name': 'Olivia',
            'author_surname': 'Jones',
            'author_alias': 'oliviajones',
            'country': 'Singapore',
            'city': 'Singapore',
            'address': '505 Orchard Road',
            'date': timezone.now() + timezone.timedelta(days=80),
            'description': 'Innovative startups pitch their ideas to investors.',
            'tags': ['startup', 'pitch', 'night']
        },
        {
            'event_name': 'Fashion Show 2024',
            'author_email': 'sophia.martin@example.com',
            'author_name': 'Sophia',
            'author_surname': 'Martin',
            'author_alias': 'sophiamartin',
            'country': 'Spain',
            'city': 'Madrid',
            'address': '606 Gran Via',
            'date': timezone.now() + timezone.timedelta(days=90),
            'description': 'Top designers showcase their latest collections.',
            'tags': ['fashion', 'show', '2024']
        },
        {
            'event_name': 'Gaming Expo 2024',
            'author_email': 'james.wright@example.com',
            'author_name': 'James',
            'author_surname': 'Wright',
            'author_alias': 'jameswright',
            'country': 'Japan',
            'city': 'Tokyo',
            'address': '707 Shibuya',
            'date': timezone.now() + timezone.timedelta(days=100),
            'description': 'The latest in video game technology and releases.',
            'tags': ['gaming', 'expo', '2024']
        }
    ]

    for request in requests:
        Events.objects.create(**request)

class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_first_data),
    ]
