# Generated by Django 2.1.7 on 2019-03-01 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handy_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_todo',
            field=models.ManyToManyField(related_name='dojob', to='handy_app.User'),
        ),
    ]
