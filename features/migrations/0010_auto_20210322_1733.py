# Generated by Django 2.2 on 2021-03-22 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0009_auto_20180318_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='number',
        ),
        migrations.AlterField(
            model_name='members',
            name='email',
            field=models.EmailField(max_length=250),
        ),
        migrations.AlterField(
            model_name='members',
            name='password',
            field=models.CharField(max_length=500),
        ),
    ]