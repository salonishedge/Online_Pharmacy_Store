# Generated by Django 2.2 on 2019-10-31 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0021_auto_20191101_0120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='username',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='post',
            name='numberofproducts',
        ),
        migrations.RemoveField(
            model_name='post',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='post',
            name='total',
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
