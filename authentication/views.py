from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import UpdateView

from .forms import UserForm, UserUpdateForm
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
class LogoutUserView(View):
    def post(self, request):
        logout(request)
        return redirect("index-page")

# view for update user
# TODO добавить permission для того чтобы не могли пользователи изменять друг-друга
class UserUpdateView(UpdateView):
    queryset = User.objects.all()
    template_name = "authentication/registration.html"
    form_class = UserUpdateForm
    success_url = "/users/profile/"


# view for delete user
# FIXME: пофиксить проблему с параметром (узнать возможно про то правильно ли передавать просто user из request)
class UserDestroyView(View):
    def post(self, request):
        request.user.delete()
        logout(request)
        return redirect("index-page")

# view for user profile
class UserProfileView(View):
    def get(self, request):
        # redirect to main page if user isn't authorizated
        # TODO возможно лучше просто наложить permission
        if not request.user.is_authenticated:
            return redirect("index-page")

        return render(request, "authentication/profile.html")


