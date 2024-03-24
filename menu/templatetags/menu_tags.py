from django import template

from menu.models import Menu

register = template.Library()


def render_menu(request, menu_items):
    html = ''
    for item in menu_items:
        is_active = False
        if item.url == request.path or item.url == request.path_info or item.url == request.resolver_match.view_name:
            is_active = True
        sub_menu = item.menu_items_set.all()
        sub_menu_html = render_menu(request, sub_menu)
        html += (f'<li class="{"active" if is_active else ""}"><a href="{item.url}">'
                 f'{item.name}</a>{sub_menu_html}</li>')
        if html:
            html = f'<ul>{html}</ul>'
        return html


@register.simple_tag(takes_context=True)
def draw_menu(context, name_menu):
    request = context['request']
    # Получаем родительские пункты меню. prefetch_related для предварительной загрузки связанных подпунктов меню.
    parent_menu = Menu.objects.filter(name=name_menu, parent=None).prefetch_related('menu_items_set')
    return render_menu(request, parent_menu)
