# Generated by Django 3.0.8 on 2020-07-05 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information',
            name='director',
        ),
    ]