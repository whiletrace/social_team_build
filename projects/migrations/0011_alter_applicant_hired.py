# Generated by Django 3.2 on 2021-05-28 11:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('projects', '0010_alter_applicant_hired'),
        ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='hired',
            field=models.BooleanField(null=True),
            ),
        ]