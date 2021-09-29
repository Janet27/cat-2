from django.shortcuts import render
from .models import CarMake, carInstance, CarModel,CarType, Car,CarOwner
from django.views.generic import ListView
# Create your views here.

def index(request):
    """View function to specify the site homepage"""

    #generate a count of all the cars in the system
    cars_count = Car.objects.all().count()
    car_instance_count = carInstance.objects.all().count()

    #count the number of available cars
    num_cars_available = carInstance.objects.filter(status__exact ='a').count()

    number_of_visits = request.session.get('number_of_visits', 0)
    request.session['number_of_visits'] = number_of_visits + 1


    #count the number of toyotas
    #num_toyota = Car.objects.filter(car_make__exact = 'Toyota').count()
#context specifies how  the data will be presenrted in the renderred view
    context = {
        'cars_count' : cars_count,
        'num_cars available': num_cars_available,
        'car_instance_count': car_instance_count,
        'number_of_visits': number_of_visits,
        #'num_toyota':num_toyota
    }

    #render a html file index .html containing the data in context

    return render(request, 'index.html', context=context)

class CarList(ListView):
    model = Car    