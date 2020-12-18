from django.http import HttpResponse


def home(request):
    return HttpResponse('Home page!')

def contact(request):
    return HttpResponse('Contact page!')