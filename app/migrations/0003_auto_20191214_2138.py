# Generated by Django 3.0 on 2019-12-14 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191214_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='picture',
            field=models.ImageField(default='app/static/img/default_item.jpg', upload_to='app/static/img/item/1105633064/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='app/static/img/default.jpg', upload_to='app/static/img/profile_pictures/1105633064/'),
        ),
    ]
