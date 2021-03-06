# Generated by Django 3.1.3 on 2020-12-04 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20201202_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('og_tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='home.tweet')),
            ],
        ),
    ]
