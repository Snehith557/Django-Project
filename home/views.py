from django.shortcuts import render
# from django.http import HttpRequest,HttpResponse
from django.shortcuts import render

# Create your views here.

def homePage(request):

    return render(request,'homepage.html')