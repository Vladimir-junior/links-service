# Generated by Django 5.0.4 on 2024-11-03 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_alter_link_url_link_unique_user_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='collection',
            old_name='updated_date',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='link',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='link',
            old_name='updated_date',
            new_name='updated_at',
        ),
    ]
