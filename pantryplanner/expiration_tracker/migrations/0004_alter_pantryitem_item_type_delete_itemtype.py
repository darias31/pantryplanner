# Generated by Django 5.1.1 on 2024-10-03 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expiration_tracker', '0003_rename_item_name_pantryitem_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pantryitem',
            name='item_type',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='ItemType',
        ),
    ]
