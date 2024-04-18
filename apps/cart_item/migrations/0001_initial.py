# Generated by Django 4.1.13 on 2024-04-17 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carts', '0001_initial'),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_item', to='carts.cart')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_item', to='items.item')),
            ],
            options={
                'db_table': 'cart_item',
                'unique_together': {('cart_id', 'item_id')},
            },
        ),
    ]