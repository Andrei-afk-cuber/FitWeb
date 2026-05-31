from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.http import HttpResponse

from .forms import UserForm
from .models import User

# view for user registration
def register_user(request):
    if request.user.is_authenticated:
        return redirect('index-page')

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)

            return redirect('login-view')
        # TODO сделать чтобы что-то происходило при невалидных данных
        return HttpResponse(form.errors)
    form = UserForm()
    data = {
        'form': form
    }

    return render(request,'authentication/registration.html', data)

# view for authorization
def user_login(request):
    if request.user.is_authenticated:
        return redirect('index-page')

    success = True
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            return redirect('index-page')

        success = False

    return render(request,'authentication/login.html', {'success': success})

# view for logout
def user_logout(request):
    logout(request)
    return redirect('index-page')