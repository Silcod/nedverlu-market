# Generated by Django 2.2.7 on 2019-12-07 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_order_ref_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slider')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
