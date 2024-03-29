# Generated by Django 4.0.6 on 2022-07-08 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('price', models.FloatField(default=0)),
                ('description', models.CharField(max_length=2500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products')),
                ('stock', models.IntegerField(default=0)),
            ],
        ),
    ]
