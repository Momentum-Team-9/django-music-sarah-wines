# Generated by Django 3.2.6 on 2021-08-16 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Album', '0004_alter_album_album_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_photo',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
