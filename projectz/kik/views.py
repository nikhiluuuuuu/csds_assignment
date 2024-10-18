from django.shortcuts import render
from kik.models import *
def hello(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')
def registered(request):
    if request.method=='POST':
        username = request.POST['user']
        password = request.POST['password']
        cpassword = request.POST['confirm_password']
        email = request.POST['mail']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        phone = request.POST['mobile']
        age = request.POST['age']
        check_user = register.objects.filter(username=username)
        if not check_user.exists():
            if password== cpassword:
                new_user=register(username=username,password=password,email=email,first_name=first_name,last_name=last_name,age=age)
                new_user.save()
                return render(request,'login.html')
            else:
                return render(request,'registration.html')
    return render(request,'registration.html')