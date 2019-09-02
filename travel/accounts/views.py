from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth 

# Create your views here.
def login(request):
        if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']

                user = auth.authenticate(username=username, password=password)
                if user is not None:
                        auth.login(request, user)
                        return redirect('/')
                else:
                        messages.info(request, 'Invalid Username and password')
                        return redirect('login')
        else:
                return render(request, 'login.html')

def register(request):
        if request.method =='POST':
                first_name = request.POST['first_name']
                username = request.POST['username']
                email = request.POST['email']
                password = request.POST['password']
                confirm_password = request.POST['password1']

                if password==confirm_password:
                        if User.objects.filter(username=username).exists():
                                messages.info(request, 'Username Taken')
                                return redirect('register')
                        elif User.objects.filter(email=email).exists():
                                messages.info(request, 'Email already used')
                                return redirect('register')
                        else:
                                user = User.objects.create_user(first_name=first_name, username=username, email=email, password=password)
                                user.save()
                                messages.info(request, 'Resister Sucessfull')
                                return redirect('login')
                else:
                        messages.info(request, 'Pass Does not match')
                        return redirect('register')
        else:
                return render(request, 'register.html')

def logout(request):
        auth.logout(request)
        return redirect('/')