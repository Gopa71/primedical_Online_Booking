from .models import Service


def menu_links(req):
    links=Service.objects.all()
    return dict(links=links)