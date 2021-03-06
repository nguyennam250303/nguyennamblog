# Generated by Django 3.2.9 on 2021-11-24 13:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Theblog', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now()),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
