# Generated by Django 3.0.7 on 2020-07-08 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_tests', '0012_test_d'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, null=True)),
                ('password', models.CharField(max_length=20, null=True)),
                ('add_test', models.BooleanField(default=True)),
                ('add_student', models.BooleanField(default=True)),
            ],
        ),
    ]