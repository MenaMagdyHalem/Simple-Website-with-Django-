# Generated by Django 3.2.6 on 2021-09-05 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20210905_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='details',
            field=models.CharField(max_length=1000),
        ),
    ]