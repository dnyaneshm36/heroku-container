# Generated by Django 3.1.2 on 2021-02-04 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='image',
        ),
    ]
