# views.py
from django.shortcuts import render, redirect
from .forms import MenuItemForm

def add_menu_item(request):
    print("Request method:", request.method)

    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            menu_item = form.cleaned_data
            menu_item['price'] = str(menu_item['price'])
            menu_items = request.session.get('menu_items', [])
            menu_items.append(menu_item)
            request.session['menu_items'] = menu_items
            request.session.modified = True
            form = MenuItemForm()
            print("Form is valid, menu item added:", menu_item)
        else:
            print("Form is not valid")
    else:
        form = MenuItemForm()

    menu_items = request.session.get('menu_items', [])
    print("Menu items in session:", menu_items)
    
    # Sort the items by type in the desired order
    categories = ["APPETIZER", "MAIN", "DESSERT", "DRINK"]
    menu_items.sort(key=lambda item: categories.index(item['type']))

    return render(request, 'menuform.html', {'form': form, 'menu_items': menu_items, 'categories': categories})



def delete_menu_item(request):
    if request.method == 'POST':
        item_index = int(request.POST['item_index'])
        menu_items = request.session.get('menu_items', [])
        if 0 <= item_index < len(menu_items):
            del menu_items[item_index]
            request.session['menu_items'] = menu_items
    return redirect('add_menu_item')
