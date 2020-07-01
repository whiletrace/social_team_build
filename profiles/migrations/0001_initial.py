# Generated by Django 3.0.6 on 2020-07-01 19:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('avatar',
                 models.ImageField(blank=True, upload_to='user_profile')),
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL)),
                ],
            ),
        ]
