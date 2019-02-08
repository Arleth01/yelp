from django.shortcuts import render

def tacos(request):
    return render(request, 'yelp/taco.html')
