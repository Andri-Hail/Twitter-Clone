# Generated by Django 3.1.3 on 2020-12-02 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
