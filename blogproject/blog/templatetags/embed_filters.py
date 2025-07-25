from django import template
import micawber
import micawber.providers
from bs4 import BeautifulSoup

register = template.Library()
providers = micawber.bootstrap_basic()

@register.filter
def render_embeds(value):
    soup = BeautifulSoup(value, "html.parser")
    for tag in soup.find_all("oembed"):
        url = tag.get("url")
        if url:
            html = providers.request(url).get("html")
            tag.replace_with(BeautifulSoup(html, "html.parser"))
    return str(soup)