# Generated by Django 4.0.3 on 2022-04-05 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_seller_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('product_id', models.CharField(max_length=50)),
                ('store_id', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('product_image', models.ImageField(default='mainapp/images', null=True, upload_to='mainapp/images/')),
            ],
        ),
    ]