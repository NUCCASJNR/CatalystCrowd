# Generated by Django 5.0 on 2023-12-21 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowd_funding', '0003_alter_project_project_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.CharField(default='miscellaneous', max_length=255),
        ),
    ]