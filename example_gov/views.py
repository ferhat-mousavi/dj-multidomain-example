from django.http import HttpResponse


def landing_page(request):
    return HttpResponse('example.gov', content_type="text/plain")
