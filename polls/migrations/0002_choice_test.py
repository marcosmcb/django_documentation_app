# Generated by Django 2.2 on 2018-07-05 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='test',
            field=models.IntegerField(default=0),
        ),
    ]
