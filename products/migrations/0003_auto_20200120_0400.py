# Generated by Django 3.0.2 on 2020-01-20 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_comment_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='comments',
            field=models.ManyToManyField(to='products.Comment'),
        ),
    ]
