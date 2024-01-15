from django.http import HttpResponse


def landing_page(request):
    return HttpResponse('example.com', content_type="text/plain")
