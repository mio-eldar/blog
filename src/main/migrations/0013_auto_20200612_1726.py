# Generated by Django 3.0.7 on 2020-06-12 17:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200612_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='subscriptions',
            field=models.ManyToManyField(related_name='subscribers', through='main.Subscription', to=settings.AUTH_USER_MODEL),
        ),
    ]
