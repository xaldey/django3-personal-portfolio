# Generated by Django 3.2.6 on 2021-08-31 09:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_published', models.DateField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
            ],
        ),
    ]
