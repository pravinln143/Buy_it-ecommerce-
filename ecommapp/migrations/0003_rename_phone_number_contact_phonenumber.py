# Generated by Django 5.1 on 2024-08-29 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0002_alter_contact_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='phone_number',
            new_name='phonenumber',
        ),
    ]
