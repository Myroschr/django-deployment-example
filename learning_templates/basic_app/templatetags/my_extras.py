from django import template
from django.utils.safestring import mark_safe
register = template.Library()

@register.filter
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!!
    """
    
    return value.replace(arg,'ggg')




@register.filter
def value(value):
    value = int(value)
    if value > 50:
        return mark_safe("<pstyle='color: red;'>Yes</p>")
    else:
        return mark_safe("<p style='color: blue;'>Not</i>")
