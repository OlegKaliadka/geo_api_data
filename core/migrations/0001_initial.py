# Generated by Django 3.2.8 on 2021-10-19 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ip', models.CharField(blank=True, max_length=30, null=True)),
                ('type_ip', models.CharField(blank=True, max_length=10, null=True)),
                ('continent_name', models.CharField(blank=True, max_length=20, null=True)),
                ('country_name', models.CharField(blank=True, max_length=40, null=True)),
                ('region_name', models.CharField(blank=True, max_length=40, null=True)),
                ('city', models.CharField(blank=True, max_length=40, null=True)),
                ('zip', models.CharField(blank=True, max_length=20, null=True)),
                ('latitude', models.DecimalField(decimal_places=40, max_digits=40)),
                ('longitude', models.DecimalField(decimal_places=40, max_digits=40)),
                ('datetime', models.DateField(blank=True, max_length=50, null=True)),
            ],
            options={
                'ordering': ['-datetime'],
            },
        ),
    ]
