# Generated by Django 4.0.6 on 2022-07-29 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0002_post_title_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='<django.db.models.fields.CharField>', max_length=255),
        ),
    ]
