# Generated by Django 3.1.4 on 2020-12-01 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatPic', '0002_auto_20201201_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pic',
            name='pic_url',
            field=models.ImageField(upload_to='CatPicPics'),
        ),
    ]
