# Generated by Django 4.1.3 on 2023-01-19 04:24

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0015_delete_friendz'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=True, editable=False, populate_from='title'),
        ),
    ]