# Generated by Django 4.1.5 on 2023-02-02 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0025_post_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
    ]
