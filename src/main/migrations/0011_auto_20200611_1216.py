# Generated by Django 3.0.7 on 2020-06-11 12:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200610_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='read_by',
            field=models.ManyToManyField(blank=True, null=True, related_name='users_read', to=settings.AUTH_USER_MODEL),
        ),
    ]
