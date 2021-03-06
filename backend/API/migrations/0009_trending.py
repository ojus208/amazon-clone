# Generated by Django 3.2 on 2021-07-29 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0008_auto_20210729_2026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.ImageField(default='', upload_to='posters')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.products')),
            ],
        ),
    ]
