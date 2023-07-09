from django.http import HttpResponse


def index(request):
    return HttpResponse('Домашка по 4 заданию')
