# Generated by Django 3.2.4 on 2021-06-03 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0006_like'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='like',
            constraint=models.UniqueConstraint(fields=('user', 'publication'), name='user_and_publication_unique'),
        ),
    ]
