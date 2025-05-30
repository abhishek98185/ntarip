from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def jeeadvance(request):
    return render(request,'jeeadvance.html')

def jee(request):
    return render(request,'jee.html')

def neet(request):
    return render(request,'neet.html')

def formulasheet(request):
    return render(request,'formulasheet.html')

def about(request):
    return render(request,'about.html')
def todolist(request):
    return render(request,'to-do.html')


