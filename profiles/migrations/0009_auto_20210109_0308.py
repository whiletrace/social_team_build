# Generated by Django 3.0.6 on 2021-01-09 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20201107_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='skills',
            field=models.ManyToManyField(related_name='profile_skills', to='profiles.Skills'),
        ),
    ]
