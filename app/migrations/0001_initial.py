# Generated by Django 3.0 on 2019-12-14 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=70)),
                ('picture', models.ImageField(default='app/static/img/default_item.jpg', upload_to='app/static/img/item/1602914588/')),
                ('descricao', models.CharField(max_length=5000)),
                ('short', models.CharField(max_length=50)),
                ('preco', models.DecimalField(decimal_places=2, default=0, max_digits=11)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('picture', models.ImageField(default='app/static/img/default.jpg', upload_to='app/static/img/profile_pictures/1602914588/')),
                ('morada', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=20)),
                ('pais', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Items')),
            ],
        ),
        migrations.CreateModel(
            name='Encomenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now=True)),
                ('user', models.CharField(max_length=50)),
                ('quantidade', models.IntegerField(default=1)),
                ('preco', models.DecimalField(decimal_places=2, default=0, max_digits=11)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=11)),
                ('produtos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Items')),
            ],
        ),
    ]