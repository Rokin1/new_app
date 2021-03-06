# Generated by Django 3.2.4 on 2021-06-24 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='duration',
            field=models.IntegerField(default=2, help_text='Enter number of hours'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lecture',
            name='is_required',
            field=models.BooleanField(default=True),
        ),
    ]
