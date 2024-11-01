# Generated by Django 5.0.4 on 2024-11-01 17:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.URLField(),
        ),
        migrations.AddConstraint(
            model_name='link',
            constraint=models.UniqueConstraint(fields=('owner', 'url'), name='unique_user_link'),
        ),
    ]
