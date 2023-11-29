# Generated by Django 4.2.7 on 2023-11-29 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_cartitem_region_storesalesperson_storetransaction_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storesalesperson',
            name='id',
        ),
        migrations.RemoveField(
            model_name='storetransaction',
            name='id',
        ),
        migrations.AddField(
            model_name='storetransaction',
            name='salesperson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='store.storesalesperson'),
        ),
        migrations.AlterField(
            model_name='storesalesperson',
            name='salesperson_ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='storetransaction',
            name='transaction_id',
            field=models.CharField(default=0, max_length=200, primary_key=True, serialize=False),
        ),
    ]
