# Generated by Django 2.2 on 2019-10-30 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainpage', '0012_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=50)),
                ('total', models.IntegerField()),
                ('phonenumber', models.IntegerField()),
            ],
            options={
                'db_table': 'Product',
            },
        ),
    ]