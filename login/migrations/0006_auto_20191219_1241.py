# Generated by Django 3.0 on 2019-12-19 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20191219_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match_list',
            name='end_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match_list',
            name='final_team1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='match_list',
            name='invisble_comments',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='match_list',
            name='start_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match_list',
            name='winner',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
