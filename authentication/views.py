from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
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

        return render(request, "authentication/registration.html", {"form": form})

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
class LogoutUserView(LoginRequiredMixin, View):
    def post(self, request):
        logout(request)
        return redirect("index-page")


# view for update user
class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    queryset = User.objects.all()
    template_name = "authentication/registration.html"
    form_class = UserUpdateForm
    success_url = reverse_lazy("profile-page")

    # Current user check
    def test_func(self):
        user_to_edit = self.get_object()
        return self.request.user == user_to_edit

    def handle_no_permission(self):
        return redirect("index-page")


# view for delete user
class UserDestroyView(LoginRequiredMixin, View):
    def post(self, request):
        request.user.delete()
        logout(request)
        return redirect("index-page")


# view for user profile
class UserProfileView(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request):
        return render(request, "authentication/profile.html")

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect("index-page")