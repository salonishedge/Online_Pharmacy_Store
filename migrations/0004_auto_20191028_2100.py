# Generated by Django 2.2 on 2019-10-28 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0003_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
