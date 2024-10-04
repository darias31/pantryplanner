from django.db import models


class PantryItem(models.Model):
    item_type = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    quantity = models.DecimalField(
        max_digits=10, decimal_places=2
    )  # For tracking units (e.g., kg, liters)
    unit = models.CharField(max_length=50)  # e.g., "kg", "grams", "liters"
    purchase_date = models.DateField(null=True)  # Optional field for purchase tracking
    expiration_date = models.DateField("Expiration Date")

    def __str__(self):
        return f"{self.item_type} - {self.brand}, exp. {self.expiration_date.month}/{self.expiration_date.day}"
