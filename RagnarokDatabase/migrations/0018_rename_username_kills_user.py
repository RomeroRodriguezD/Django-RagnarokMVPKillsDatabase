# Generated by Django 4.0.6 on 2022-07-11 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RagnarokDatabase', '0017_rename_user_kills_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kills',
            old_name='username',
            new_name='user',
        ),
    ]
