# Generated by Django 4.0.3 on 2022-05-20 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
