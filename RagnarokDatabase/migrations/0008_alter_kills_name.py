# Generated by Django 4.0.6 on 2022-07-11 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RagnarokDatabase', '0007_alter_kills_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kills',
            name='name',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
