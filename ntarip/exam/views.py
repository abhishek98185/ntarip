from django.shortcuts import render

# Create your views here.

def exam(request,year, paper):
    return render(request, 'jeemains.html')
