from django.shortcuts import render

def menu_list(request):
    items = [
        {"name": "Burger", "category": "Main", "price": 150, "available": True},
        {"name": "Orange Juice", "category": "Drinks", "price": 50, "available": True},
        {"name": "Ice Cream", "category": "Dessert", "price": 60, "available": True},
        {"name": "Chocolate Cake", "category": "Dessert", "price": 80, "available": True},
        {"name": "Pizza", "category": "Main", "price": 200, "available": False},
    ]

    search_q = request.GET.get('search', '')
    category_q = request.GET.get('category', '')

    
    if search_q:
        items = [i for i in items if search_q.lower() in i['name'].lower()]
    
    if category_q and category_q != "All":
        items = [i for i in items if i['category'] == category_q]

    return render(request, 'menu/search.html', {
        'items': items,
        'last_search': search_q,
        'last_category': category_q
    })