from django.shortcuts import render, get_object_or_404
from .models import Menu

def menu_page(request, menu_url, item_id=None):
    menu = get_object_or_404(Menu, url=menu_url)
    return render(request, "menu_page.html", {
        "menu": menu
    })