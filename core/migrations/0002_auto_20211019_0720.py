# Generated by Django 3.2.8 on 2021-10-19 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermodel',
            options={},
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='datetime',
        ),
    ]
