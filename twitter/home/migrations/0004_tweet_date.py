# Generated by Django 3.1.3 on 2020-12-01 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201201_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
