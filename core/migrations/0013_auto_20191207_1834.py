# Generated by Django 2.2.7 on 2019-12-07 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_slider_img_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='image',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='img_name',
        ),
        migrations.AddField(
            model_name='slider',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='slider'),
        ),
        migrations.AddField(
            model_name='slider',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='slider'),
        ),
        migrations.AddField(
            model_name='slider',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='slider'),
        ),
        migrations.AddField(
            model_name='slider',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='slider'),
        ),
        migrations.AddField(
            model_name='slider',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='slider'),
        ),
        migrations.AddField(
            model_name='slider',
            name='image6',
            field=models.ImageField(blank=True, null=True, upload_to='slider'),
        ),
    ]
