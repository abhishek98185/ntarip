from django.shortcuts import render, get_object_or_404, redirect
from home.models import Contact, Profile
from django.contrib.auth.decorators import login_required

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
@login_required
def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        user_class = request.POST.get('student_class')
        image = request.FILES.get('image')

        if username:
            request.user.username = username
        if email:
            request.user.email = email
        request.user.save()


        profile.user_class = user_class
        if image:
            profile.image = image 
        profile.save()

        return redirect('profile')
    return render(request, 'profile.html', {
        'name': profile.user.username,
        'email': profile.user.email,
        'image': profile.image,
        'user_class': profile.user_class
    })
      
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



