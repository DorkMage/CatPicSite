# Generated by Django 3.1.4 on 2020-12-06 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatPic', '0007_auto_20201206_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pic',
            name='pic_id',
            field=models.CharField(default='CatPic000', max_length=16, primary_key=True, serialize=False, unique=True),
        ),
    ]
