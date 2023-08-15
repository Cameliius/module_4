from django.http import HttpResponse
from django.shortcuts import render

from .models import Adverisments


def index(request):
    adverisments = Adverisments.objects.all()
    context = {'adverisments': adverisments}
    return render(request, 'index.html', context)


def top_sellers(request):
    return render(request, 'top-sellers.html')
