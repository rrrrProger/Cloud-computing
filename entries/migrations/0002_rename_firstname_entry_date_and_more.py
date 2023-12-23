# Generated by Django 5.0 on 2023-12-23 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='firstname',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='lastname',
            new_name='purpose',
        ),
        migrations.AddField(
            model_name='entry',
            name='time_on_task',
            field=models.IntegerField(default=0),
        ),
    ]
