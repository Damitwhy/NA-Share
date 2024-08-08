# core/templatetags/extras.py
from django import template
import bleach
from bs4 import BeautifulSoup

register = template.Library()

@register.filter(name='truncate_words')
def truncate_words(value, arg):
    try:
        length = int(arg)
    except ValueError:
        return value  # Invalid argument, return the original value

    soup = BeautifulSoup(value, "html.parser")
    text = soup.get_text()
    words = text.split()
    
    if len(words) > length:
        truncated_text = ' '.join(words[:length]) + '...'
    else:
        truncated_text = text

    truncated_html = bleach.clean(truncated_text, tags=[], strip=True)
    return truncated_html


@register.filter(name='capitalize_first')
def capitalize_first(value):
    if not isinstance(value, str) or not value:
        return value
    words = value.split()
    words[0] = words[0].capitalize()
    return ' '.join(words)