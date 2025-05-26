from django.shortcuts import render

# Create your views here.

def exam(request, year, name):
    return render(request, 'jeemains.html')
