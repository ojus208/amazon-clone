# Generated by Django 3.2 on 2021-07-29 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0006_auto_20210729_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('poster', models.ImageField(default='', upload_to='posters')),
                ('products', models.ManyToManyField(to='API.Products')),
            ],
        ),
    ]
