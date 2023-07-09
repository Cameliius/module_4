from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1 style="text-align: center; background-color: yellow">Всё ок!</h1>')
