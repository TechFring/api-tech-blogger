# Generated by Django 3.2.4 on 2021-06-11 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='total_publications',
            field=models.IntegerField(default=0),
        ),
    ]
