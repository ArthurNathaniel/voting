# Generated by Django 4.1.7 on 2023-06-08 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting_app', '0002_remove_nominee_event_name_nominee_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nominee',
            name='event',
            field=models.CharField(choices=[('miss_toss', 'miss_toss'), ('miss_src', 'Miss SRC'), ('talent_expo', 'Talent Expo')], default='your_default_value', max_length=50),
        ),
    ]