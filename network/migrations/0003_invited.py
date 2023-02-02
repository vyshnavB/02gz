# Generated by Django 4.1.3 on 2023-01-11 05:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_alter_inviters_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='invited',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fr', models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, related_name='frinvit', to=settings.AUTH_USER_MODEL)),
                ('to', models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, related_name='toinvit', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
