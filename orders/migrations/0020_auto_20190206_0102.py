# Generated by Django 2.1 on 2019-02-06 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_auto_20190206_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrymodel',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart_entries', to='orders.CartModel'),
        ),
    ]
