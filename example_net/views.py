from django.http import HttpResponse


def landing_page(request):
    return HttpResponse('example.net', content_type="text/plain")
