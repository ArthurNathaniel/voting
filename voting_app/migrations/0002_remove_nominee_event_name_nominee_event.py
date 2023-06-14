# Generated by Django 4.1.7 on 2023-06-08 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nominee',
            name='event_name',
        ),
        migrations.AddField(
            model_name='nominee',
            name='event',
            field=models.CharField(choices=[('miss_toss', 'Miss Toss'), ('miss_src', 'Miss SRC'), ('talent_expo', 'Talent Expo')], default='your_default_value', max_length=50),
        ),
    ]