from bs4 import BeautifulSoup
from django.utils.html import escape

excluded_tags = ['script', 'iframe']
def sanitize_content(content):
    """
    Sanitize content body to prevent xss attacks.
    """
    soup = BeautifulSoup(content, 'html.parser')
    for tag in soup.find_all():
        if tag.name in excluded_tags:
            tag.replace_with(escape(tag))
    
    for img in soup.find_all('img'):
        if img.has_attr('onload'):
            del img['onload']

    return soup.prettify()


