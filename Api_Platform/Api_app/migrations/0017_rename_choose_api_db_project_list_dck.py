# Generated by Django 3.2.13 on 2022-09-09 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api_app', '0016_db_apis'),
    ]

    operations = [
        migrations.RenameField(
            model_name='db_project_list',
            old_name='choose_api',
            new_name='dck',
        ),
    ]
