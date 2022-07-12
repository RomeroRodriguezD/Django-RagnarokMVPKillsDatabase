# Generated by Django 4.0.6 on 2022-07-11 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('RagnarokDatabase', '0013_alter_kills_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kills',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
