# Generated by Django 2.1.3 on 2018-11-17 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='join_date',
            field=models.DateTimeField(default=None, verbose_name='date joined'),
            preserve_default=False,
        ),
    ]
