from django.db import migrations

def add_initial_data(apps, schema_editor):
    Alumni = apps.get_model('card_request', 'Alumni')

    requests = [
        {'email': 'o.grediushko@innopolis.university', 'name': 'Olesia', 'surname': 'Grediushko',
         'telegram': '@WellNotWell', 'graduation_year': 2022},
        {'email': 'j.smith@innopolis.university', 'name': 'Jane', 'surname': 'Smith',
         'telegram': '@janesmith', 'graduation_year': 2021},
        {'email': 'a.brown@innopolis.university', 'name': 'Alice', 'surname': 'Brown',
         'telegram': '@alicebrown', 'graduation_year': 2015},
    ]

    for request in requests:
        Alumni.objects.create(**request)

class Migration(migrations.Migration):

    dependencies = [
        ('card_request', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_data),
    ]
