from django.shortcuts import render
from .models import Sauce, Sandwich

# Create your views here.
def home(request):

    sandwich = Sandwich.objects.filter(sauces__name="Sauce2")
    sauces = Sauce.objects.filter(sandwiches__name="Sandwich3")
    context = {
    "sauces": sauces,
    }

    return render(request, 'index.html', context)
