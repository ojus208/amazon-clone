# Generated by Django 3.2 on 2021-08-04 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0016_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='deals',
            name='banner',
            field=models.ImageField(blank=True, default='', upload_to='posters'),
        ),
    ]