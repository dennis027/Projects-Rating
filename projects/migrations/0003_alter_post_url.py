# Generated by Django 3.2.5 on 2021-07-19 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]
