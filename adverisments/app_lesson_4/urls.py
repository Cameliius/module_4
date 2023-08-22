from django.urls import path

from .views import index, top_sellers, adverisments_post


urlpatterns = [
    path("", index, name='main-page'),
    path('top-sellers/', top_sellers, name = 'top-sellers'),
    path('adverisments_post/', adverisments_post, name = 'adv_post')
]