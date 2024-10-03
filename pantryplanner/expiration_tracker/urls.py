from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pantry_item_list/", views.PantryItemListView.as_view(), name="pantry_item_list"),
]