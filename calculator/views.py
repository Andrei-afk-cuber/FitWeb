from django.shortcuts import render
from django.views import View


# main calculator view
class CalculatorView(View):
    def get(self, request):
        return render(request, "calculator/main.html")