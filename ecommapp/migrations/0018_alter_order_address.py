# Generated by Django 5.1 on 2024-09-10 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0017_alter_order_payment_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
