# Generated by Django 2.2 on 2019-10-31 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0018_auto_20191031_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hotel_Main_Img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]