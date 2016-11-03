from django.shortcuts import render
from django.http import HttpResponse
from space.models import Planet
from space.forms import PlanetForm
import json


def planet_list(request):
    planets = Planet.objects.all()[:20]
    get_param = request.GET.get('example', 'EMPTY')
    return render(
        request, 'space/planet_list.html',
        {'planets': planets, 'get_param': get_param, 'user': request.user}
    )


def planet_list_json(request):
    planets = list(Planet.objects.values(
        'name', 'description'
    )[:20])
    return HttpResponse(json.dumps(planets), content_type='text/json')


def planet_create(request):
    if request.method == 'POST':
        form = PlanetForm(request.POST)
        if form.is_valid():
            form.save() 
    else:
        form = PlanetForm()

    return render(
        request, 'space/planet_create.html',
        {'form': form}
    )
        
