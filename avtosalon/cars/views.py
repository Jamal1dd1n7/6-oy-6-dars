from django.shortcuts import render, get_object_or_404
from django.core.handlers.wsgi import WSGIRequest
from .models import Car, Brend
from .models import Car

def home(request: WSGIRequest):
    brends = Brend.objects.all()
    cars = Car.objects.all()
    context = {
        "brends": brends,
        "cars": cars
    }
    return render(request, "intex.html", context)

def brend(request, brend_id):
    brends = Brend.objects.all()
    cars = Car.objects.filter(brend_id = brend_id)

    context = {
        "brends": brends,
        "cars": cars
    }
    return render(request, "index.html", context)

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    car.views += 1
    car.save()
    return render(request, 'intex2.html', {'car': car})