# Generated by Django 5.0 on 2023-12-23 17:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0003_alter_entry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]