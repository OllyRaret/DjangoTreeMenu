from django.contrib import admin
from django.urls import path
from core.views import menu_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path("<str:menu_url>/", menu_page, name="menu"),
    path("<str:menu_url>/<int:item_id>/", menu_page, name="menu_item"),
]
