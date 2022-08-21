# Generated by Django 4.1 on 2022-08-21 11:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_verified_alter_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_time',
            field=models.DateTimeField(auto_created=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='modified_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
