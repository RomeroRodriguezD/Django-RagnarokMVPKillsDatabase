# Generated by Django 4.0.6 on 2022-07-11 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RagnarokDatabase', '0009_alter_kills_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kills',
            name='user',
        ),
    ]
