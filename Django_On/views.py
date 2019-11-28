
from django.shortcuts import render
#from django.http import HttpResponse

# on lui met request car definit dans home 
def home(request):
    return render(request,'home.html')
    #HttpResponse('Bonjour Sylas')

def about(request):
    return render(request,'pages/about.html')
    #HttpResponse('Bonjour Sylas')

def contact(request):
    return render(request,'pages/contact.html')
    #HttpResponse('Bonjour Sylas')