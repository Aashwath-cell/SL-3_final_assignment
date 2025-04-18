from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import Item
from .forms import ItemForm

class ItemListView(ListView):
    model = Item
    template_name = 'items/item_list.html'
    context_object_name = 'items'

class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'items/item_form.html'
    success_url = '/' 