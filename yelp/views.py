from django.shortcuts import render
from .models import Food

def tacos(request):
    foods = Food.objects
    return render(request, 'yelp/taco.html',{
    'foods':foods
})
