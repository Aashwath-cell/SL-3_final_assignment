from django.contrib import admin
from django.urls import path
from items.views import ItemListView, ItemCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ItemListView.as_view(), name='item_list'),
    path('items/new/', ItemCreateView.as_view(), name='item_create'),
] 