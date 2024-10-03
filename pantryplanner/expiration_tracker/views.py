from django.shortcuts import render
from django.views.generic import ListView
from .models import PantryItem

def index(request):
    return render(request, 'index.html')

class PantryItemListView(ListView):
    model = PantryItem
    template_name = 'pantry_item_list.html'
    context_object_name = 'pantry_items'