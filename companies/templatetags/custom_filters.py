from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def add_class(field, css_class):
    """
    Adds a CSS class to the form field widget
    """
    return field.as_widget(attrs={'class': css_class})
