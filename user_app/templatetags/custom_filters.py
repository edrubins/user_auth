from django import template

register = template.Library()

@register.filter(name='row_class')
def row_class(value):
    new_class = ""
    if value % 2:
        new_class = "even_row"
    else:
        new_class = "odd_row"

    return new_class
