# Generated by Django 3.0.2 on 2020-01-20 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_comment_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='photo',
        ),
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
