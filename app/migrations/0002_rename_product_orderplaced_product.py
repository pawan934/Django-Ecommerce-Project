# Generated by Django 4.2 on 2023-05-25 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderplaced',
            old_name='Product',
            new_name='product',
        ),
    ]
