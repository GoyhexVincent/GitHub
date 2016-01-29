from django.shortcuts import render
from models import *
from forms import *
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.gis.geos import Point

def add_point(request):

    if request.method == 'POST':
        form = AddHouseForm(request.POST)
        if form.is_valid():
            new_point = house4sale()
            cd = form.cleaned_data
            coordinates = cd['coordinates'].split(',')
            new_point.geom = Point(float(coordinates[0]), float(coordinates[1]))
            new_point.owner = cd['owner']
            new_point.area = cd['area']
            new_point.price = cd['price']

            new_point.save()
            return HttpResponseRedirect('/add_point/success')

        else:
            return HttpResponseRedirect('/add_point/error')
    else:
        form = AddHouseForm()

    args = {}
    args.update(csrf(request))
    args['form'] = AddHouseForm()

    return render_to_response('myapp/add_point.html', args)
    
def form_error(request):
    return render_to_response('myapp/form_error.html')

def form_success(request):
    return render_to_response('myapp/form_success.html')
