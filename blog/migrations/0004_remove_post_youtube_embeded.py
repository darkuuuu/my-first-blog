# Generated by Django 4.1.5 on 2023-01-08 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_youtube_embeded'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='youtube_embeded',
        ),
    ]
