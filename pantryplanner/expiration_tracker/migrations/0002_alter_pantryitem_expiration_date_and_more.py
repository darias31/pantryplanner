# Generated by Django 5.1.1 on 2024-10-03 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expiration_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pantryitem',
            name='expiration_date',
            field=models.DateField(verbose_name='Expiration Date'),
        ),
        migrations.AlterField(
            model_name='pantryitem',
            name='purchase_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='pantryitem',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pantryitem',
            name='unit',
            field=models.CharField(max_length=50),
        ),
    ]
