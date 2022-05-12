# Generated by Django 3.2 on 2021-07-30 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0011_alter_trending_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trending',
            name='product',
        ),
        migrations.AddField(
            model_name='trending',
            name='product',
            field=models.ManyToManyField(to='API.Products'),
        ),
    ]
