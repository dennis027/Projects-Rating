# Generated by Django 3.2.5 on 2021-07-19 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_post_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='live',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]