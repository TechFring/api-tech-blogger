# Generated by Django 3.2.4 on 2021-06-03 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publications', '0002_rename_user_id_publication_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publication',
            options={'ordering': ('created_at',), 'verbose_name': 'publicação', 'verbose_name_plural': 'publicações'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ('created_at',)},
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publications.publication')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'comentário',
                'verbose_name_plural': 'comentários',
                'db_table': 'comments',
            },
        ),
    ]
