# Generated by Django 3.0.7 on 2020-06-09 18:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_profile_subscribers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='New post', max_length=255)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='subscribers',
            field=models.ManyToManyField(limit_choices_to={'profile': 'self.profile'}, related_name='subs', to=settings.AUTH_USER_MODEL),
        ),
    ]
