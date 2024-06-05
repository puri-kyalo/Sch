from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('facts/', views.facts, name='facts'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('application/', views.application, name='application'),
    path('sports/', views.sports, name='sports'),
    path('accomodations/', views.accomodations, name='accomodations'),
    path('programmes/', views.accomodations, name='programmes'),
]


