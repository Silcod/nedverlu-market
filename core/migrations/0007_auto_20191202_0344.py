# Generated by Django 2.2.7 on 2019-12-02 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_item_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
    ]
