# Generated by Django 4.2.7 on 2023-11-29 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_remove_storesalesperson_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StoreTransaction',
        ),
    ]
