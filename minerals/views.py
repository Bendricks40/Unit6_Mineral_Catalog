from django.shortcuts import render
from .models import Mineral
import random

# Create your views here.
def mineral_list(request):
    minerals = Mineral.objects.all()
    count = Mineral.objects.count()
    randMineral = random.randrange(1, count)
    return render(request, 'minerals/mineral_list.html', {'minerals': minerals, 'randMineral': randMineral})

def mineral_detail(request, pk):
    mineral = Mineral.objects.get(pk=pk)
    count = Mineral.objects.count()
    randMineral = random.randrange(1, count)
    return render(request, 'minerals/mineral_detail.html', {'mineral': mineral, 'randMineral': randMineral})