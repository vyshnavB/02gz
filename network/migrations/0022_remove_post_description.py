# Generated by Django 4.1.3 on 2023-01-25 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0021_post_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='description',
        ),
    ]