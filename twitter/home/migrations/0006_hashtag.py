# Generated by Django 3.1.4 on 2020-12-02 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_tweet_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200)),
                ('tweets', models.ManyToManyField(related_name='tag', to='home.Tweet')),
            ],
        ),
    ]