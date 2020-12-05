# Generated by Django 3.1.3 on 2020-12-05 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_tweet_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='children',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='kid', to='home.tweet'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='home.tweet'),
        ),
    ]
