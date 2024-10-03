from django import forms
from .models import PantryItem, ItemType

class PantryItemForm(forms.ModelForm):
    class Meta:
        model = PantryItem
        fields = ['item_type', 'brand', 'quantity', 'unit', 'purchase_date', 'expiration_date']
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item_type'].queryset = ItemType.objects.all()