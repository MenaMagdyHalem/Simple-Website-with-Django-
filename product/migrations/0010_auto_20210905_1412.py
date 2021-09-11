# Generated by Django 3.2.6 on 2021-09-05 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_product_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='details',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(db_column='Full name', max_length=100),
        ),
    ]