# Generated by Django 4.0.3 on 2022-03-28 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippest',
            field=models.CharField(default='click link above', max_length=255),
        ),
    ]