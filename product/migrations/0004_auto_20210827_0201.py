# Generated by Django 3.2.6 on 2021-08-27 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210826_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cost',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='details',
            field=models.CharField(default=100, max_length=1000),
            preserve_default=False,
        ),
    ]
