# Generated by Django 3.1.2 on 2020-10-31 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0011_auto_20201030_0201'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Store.cart'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cart',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='book_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
