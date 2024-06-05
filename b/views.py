from django.shortcuts import render

from b.forms import ContactForm


# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def facts(request):
    return render(request,'facts.html')

def gallery(request):
    return render(request,'gallery.html')

def contact(request):
    return render(request,'contact.html')

def application(request):
    return render(request,'application.html')

def sports(request):
    return render(request,'sports.html')

def accomodations(request):
    return render(request,'accomodations.html')

def programmes(request):
    return render(request,'programmes.html')
