from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'home.html',context)

def about(request):
    context = {}
    return render(request, 'about.html',context)

def service(request):
    context = {}
    return render(request, 'service.html',context)

def contact(request):
    context = {}
    return render(request, 'contact.html',context)

def industries(request):
    context = {}
    return render(request, 'dropdown/industries.html',context)

def offer(request):
    context = {}
    return render(request, 'dropdown/offer.html',context)

def quality(request):
    context = {}
    return render(request, 'dropdown/quality.html',context)

def choose(request):
    context = {}
    return render(request, 'dropdown/choose.html',context)