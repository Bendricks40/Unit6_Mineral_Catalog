from django.shortcuts import render
from django.http import HttpResponse

def minerals(request):
    return render(request, 'layout.html')


