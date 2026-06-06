from django.shortcuts import render
from django.views import View

from .utils import NutritionCalculator
from authentication.models import User


# main calculator view
class CalculatorView(View):
    def get(self, request):

        try:
            user = request.user
            data = {}
            # calculations
            data['bmr'] = NutritionCalculator.calculate_bmr(user.gender, user.weight, user.height, user.age)
            data['tdee'] = NutritionCalculator.calculate_tdee(data['bmr'], user.activity_status)
            data['calories'] = NutritionCalculator.calculate_daily_calories(data['tdee'], user.target)
            data = data | NutritionCalculator.calculate_macros(data['calories'], user.target, user.gender, user.weight)

            return render(request, "calculator/main.html", data)

        except AttributeError:
            return render(request, "calculator/main.html")