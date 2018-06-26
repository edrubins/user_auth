from django import template

register = template.Library()

@register.filter(name='odd_even')
def odd_even(value, choices):
    if choices is None:
        choice = ""
    else:
        if value % 2:
            choice = choices['odd']
        else:
            choice = choices['even']

    return choice