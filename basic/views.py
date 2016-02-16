"""Views."""

from django.http import HttpResponse


def hello(request):
    """Hello World."""
    return HttpResponse("Hello World")
