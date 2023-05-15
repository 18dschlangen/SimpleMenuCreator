from django.urls import path
from .views import add_menu_item, delete_menu_item

urlpatterns = [
    path('', add_menu_item, name='add_menu_item'),
    path('delete/', delete_menu_item, name='delete_menu_item'),
]