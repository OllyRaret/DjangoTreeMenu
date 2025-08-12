from django import template

from ..models import Menu

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path_info

    try:
        menu = Menu.objects.prefetch_related('items').get(name=menu_name)
    except Menu.DoesNotExist:
        return {'menu': None}

    items = list(menu.items.all().order_by('order'))

    menu_tree = []
    item_dict = {}

    for item in items:
        item_dict[item.id] = {
            'id': item.id,
            'title': item.title,
            'url': item.get_url(),
            'children': [],
            'parent': item.parent_id,
            'is_active': False,
            'is_expanded': False,
        }

    for item in items:
        if item.parent_id is None:
            menu_tree.append(item_dict[item.id])
        else:
            parent = item_dict.get(item.parent_id)
            if parent:
                parent['children'].append(item_dict[item.id])

    def mark_active_and_expanded(items, current_url):
        for item in items:
            if item['url'] == current_url:
                item['is_active'] = True
                item['is_expanded'] = True
                return True
            if mark_active_and_expanded(item['children'], current_url):
                item['is_expanded'] = True
                return True
        return False

    mark_active_and_expanded(menu_tree, current_url)

    return {
        'menu': menu,
        'menu_tree': menu_tree,
        'current_url': current_url,
    }
