from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Adverisments
from .forms import AdvertismentForm
from django.urls import reverse


def index(request):
    adverisments = Adverisments.objects.all()
    context = {'adverisments': adverisments}
    return render(request, 'app_advertisement/index.html', context)


def top_sellers(request):
    return render(request, 'app_advertisement/top-sellers.html')


def adverisments_post(request):
    if request.method == 'POST':
        form = AdvertismentForm(request.POST, request.FILES)
        if form.is_valid():
            adverisments = Adverisments(**form.cleaned_data)
            adverisments.user = request.user
            adverisments.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertismentForm()

    context = {'form': form}
    return render(request, 'app_advertisement/advertisement-post.html', context)
