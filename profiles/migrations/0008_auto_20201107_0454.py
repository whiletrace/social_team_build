# Generated by Django 3.0.6 on 2020-11-07 04:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0007_auto_20201030_2313'),
        ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    to=settings.AUTH_USER_MODEL, unique=True),
            ),
        ]