# Generated by Django 3.0 on 2019-12-18 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('user_type', models.CharField(max_length=3)),
                ('assignment_status', models.BooleanField(default=False)),
                ('asssigment_code', models.IntegerField(default=0)),
            ],
        ),
    ]
