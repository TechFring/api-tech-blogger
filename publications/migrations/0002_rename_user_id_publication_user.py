# Generated by Django 3.2.4 on 2021-06-03 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='user_id',
            new_name='user',
        ),
    ]
