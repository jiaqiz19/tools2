from django.http import HttpResponse
from .models import Pet
from .models import Sq
from django.shortcuts import render
import csv
def all_pets(request):
    pets = Pet.objects.all()
    context = {
        'pets': pets,
    }
    return render(request, 'adopt/all.html', context)

def pet_details(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    return HttpResponse(pet.name)
def sq_name(request):
     with open(/Users/doreenzhang/Desktop/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv ) as csvfile:
         reader = csv.DictReader(csvfile)
         for row in reader:
         # The header row values become your keys
            x = row[0]
            y = row[1]
         # etc....

            new_revo = Revo(X=x, Y=y)
            new_revo.save()
     sqs = new_revo.objects.all()
     context={
             'squirrels':sqs,
     }
     return render(request, 'adopt/alls.html', context)
