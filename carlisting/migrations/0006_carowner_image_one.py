# Generated by Django 3.2.6 on 2021-09-29 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carlisting', '0005_carmodel_image_one'),
    ]

    operations = [
        migrations.AddField(
            model_name='carowner',
            name='image_one',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Car Picture'),
        ),
    ]