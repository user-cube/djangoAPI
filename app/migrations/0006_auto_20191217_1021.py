# Generated by Django 3.0 on 2019-12-17 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20191214_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='picture',
            field=models.ImageField(default='app/static/img/default_item.jpg', upload_to='app/static/img/item/-536775747/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='app/static/img/default.jpg', upload_to='app/static/img/profile_pictures/-1767964520/'),
        ),
    ]