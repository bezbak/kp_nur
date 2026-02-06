from django import template

register = template.Library()


@register.filter
def space_separated(value):
    """Форматирует число с пробелами каждые 3 цифры (например: 1 000 000)"""
    try:
        value = int(value)
    except (ValueError, TypeError):
        return value
    
    # Преобразуем число в строку и добавляем пробелы
    return "{:,}".format(value).replace(",", " ")
