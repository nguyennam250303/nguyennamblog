# Generated by Django 3.2.9 on 2021-11-23 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/images'),
        ),
    ]
