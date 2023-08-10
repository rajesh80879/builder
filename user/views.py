from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from user.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password


# Create your views here.

def login_data(request):
    try:
        if request.method == "GET":
            if request.user.is_authenticated:
                return redirect('dashboard')
            return render(request, "login.html")
        
        elif request.method == "POST":
            email = request.POST["email"].lower()
            password = request.POST["password"]
        
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
            else:
                messages.error(request, "Incorrect credentials")
                return redirect("/")
            return redirect('dashboard')
        
    except Exception as ep:
        messages.error(request, "Something went Wrong")
        return redirect("/")
    
@login_required 
def dashboard(request):
    return render(request, "dashboard.html")


@login_required
def contact(request):
    if request.method == "GET":
        user = CustomUser.objects.all().exclude(id=request.user.id)
        return render(request, "contact.html",{"users":user})
    
    elif request.method == "POST":
        if all(i for i in request.POST.values()):

            name = request.POST['name']
            email = request.POST["email"].lower()
            password = request.POST["password"]

            CustomUser.objects.create(
                name=name,
                email=email,
                password=make_password(password)
            )
            messages.success(request, "User added successfully")
            return redirect("contact")

def logout_user(request):
    try:        
        logout(request)
        messages.info(request, "Logged out successfully")
        return redirect("/")
    
    except Exception as ep:
        messages.error(request, "Something went Wrong ")
        return redirect("/")


@login_required
def del_user(request, pk):
    try:
        user = CustomUser.objects.get(id=pk)
        user.delete()
        messages.success(request, "User deleted successfully")
        return redirect("contact")
        
    except Exception as ep:
        messages.error(request, "Something went Wrong ")
        return redirect("/")

