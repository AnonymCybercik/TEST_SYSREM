# Generated by Django 3.0.7 on 2020-06-28 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_tests', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='second_name',
            new_name='last_name',
        ),
    ]