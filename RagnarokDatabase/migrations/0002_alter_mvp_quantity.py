# Generated by Django 4.0.6 on 2022-07-04 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RagnarokDatabase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mvp',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
