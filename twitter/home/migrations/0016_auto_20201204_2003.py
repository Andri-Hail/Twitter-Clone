# Generated by Django 3.1.3 on 2020-12-05 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_tweet_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='parent',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.tweet'),
        ),
    ]
