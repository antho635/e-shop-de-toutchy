# Generated by Django 4.0.6 on 2022-07-09 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='orders',
            field=models.ManyToManyField(to='store.order'),
        ),
    ]
