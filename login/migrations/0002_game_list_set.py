# Generated by Django 3.0 on 2020-01-04 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game_list',
            name='set',
            field=models.IntegerField(default=1),
        ),
    ]
