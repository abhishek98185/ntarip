
from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Create your views here.

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username,password=password)
        if not User.objects.filter(username=username).exists():
            messages.info(request,"Invalid Username")
            return redirect('/account/login')
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Password")
            return redirect('/account/login')

        
    return render(request,'login.html')
def logoutUser(request):
    logout(request)
    return redirect('/account/login')

def registration(request):
    if request.method == "POST":
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already taken!")
            return redirect('/account/register')  # or return render(request, 'register.html')

        # Check if email already exists (optional)
        if User.objects.filter(email=email).exists():
            messages.info(request, "Email already registered!")
            return redirect('/account/register')

        # Create and save user
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password  # Automatically hashed by create_user
        )

        messages.success(request, "Registration successfully completed!")
        return redirect('/account/login')  # Redirect after successful registration

    return render(request, 'register.html')