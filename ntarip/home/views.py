from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def jeeadvance(request):
    return render(request,'jeeadvance.html')

def jee(request):
    return render(request,'jee.html')


