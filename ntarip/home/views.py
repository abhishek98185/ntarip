from django.shortcuts import render
from home.models import Contact
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

def dashboard(request):
    return render(request,'dashboard.html')

def profile(request):
    return render(request,'profile.html')

def leadership(request):
    return render(request,'leadership.html')

def contact(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact.objects.create(
            username = username,
            email = email,
            message = message
        )

    return render(request, 'contact.html')


