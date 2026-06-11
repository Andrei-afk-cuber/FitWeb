from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.core.cache import cache

from .utils import NutritionCalculator


# main calculator view
class CalculatorView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            user = request.user

            cache_key = f"user:{user.id}:calculation_data"
            data = cache.get(cache_key)

            if data:
                return render(request, "calculator/main.html", data)

            data = {}
            # calculations
            data["bmr"] = NutritionCalculator.calculate_bmr(
                user.gender, user.weight, user.height, user.age
            )
            data["tdee"] = NutritionCalculator.calculate_tdee(
                data["bmr"], user.activity_status
            )
            data["calories"] = NutritionCalculator.calculate_daily_calories(
                data["tdee"], user.target
            )
            data = data | NutritionCalculator.calculate_macros(
                data["calories"], user.target, user.gender, user.weight
            )

            cache.set(cache_key, data, 900)

            return render(request, "calculator/main.html", data)

        except AttributeError:
            return render(request, "calculator/main.html")
