from django.shortcuts import render
from django.views.generic import ListView
from .models import PantryItem
from rest_framework import viewsets
from .serializers import PantryItemSerializer


def index(request):
    return render(request, "index.html")


'''class PantryItemListView(ListView):
    model = PantryItem
    template_name = "pantry_item_list.html"
    context_object_name = "pantry_items"'''


class PantryItemListView(viewsets.ModelViewSet):
    serializer_class = PantryItemSerializer
    queryset = PantryItem.objects.all()
