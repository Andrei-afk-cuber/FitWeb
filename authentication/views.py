from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('index-page')
    return render(request, 'authentication/login.html')

def user_logout(request):
    pass