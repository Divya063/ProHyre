# Generated by Django 2.2.1 on 2019-05-29 17:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190529_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
