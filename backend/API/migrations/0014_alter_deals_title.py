# Generated by Django 3.2 on 2021-07-30 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0013_auto_20210730_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deals',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
