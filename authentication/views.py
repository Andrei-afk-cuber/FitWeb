from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views import View

from .forms import UserForm
from .models import User


# view for registration
class RegisterUserView(View):
    form_class = UserForm

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("index-page")

        form = self.form_class()
        data = {"form": form}

        return render(request, "authentication/registration.html", data)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)

            return redirect("login-page")
        # TODO сделать чтобы что-то происходило при невалидных данных
        return HttpResponse(form.errors)


# login view
class LoginUserView(View):
    success = True

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("index-page")

        return render(request, "authentication/login.html", {"success": self.success})

    def post(self, request):
        email = request.POST["email"]
        password = request.POST["password"]

        # user authorization
        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            return redirect("index-page")

        self.success = False

        return render(request, "authentication/login.html", {"success": self.success})


# view for logout
# FIXME: It's temp solution. Later will added button with POST method.
class LogoutUserView(View):
    def get(self, request):
        logout(request)
        return redirect("index-page")
