from django.shortcuts import render
from .models import Food 
def tacos(request):
    return render(request, 'yelp/taco.html')
