# Generated by Django 2.0.7 on 2018-08-09 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitterapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uefa',
            name='Teams',
            field=models.CharField(max_length=64),
        ),
    ]
