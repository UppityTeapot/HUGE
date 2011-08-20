# Create your views here.

from django.http import HttpResponse
from django.shortcuts import *
from storyteller.models import Place
from storyteller.models import Thing

def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def placeindex(request):
    place_list = Place.objects.all().order_by('-name')
    return render_to_response('place/detail.html', {'place_list': place_list}, context_instance=RequestContext(request))

def place(request, place_id):
    p = get_object_or_404(Place, pk=place_id)
    o = Thing.objects.filter(location=place_id)
    return render_to_response('place/detail.html', {'place': p, 'thing': o}, context_instance=RequestContext(request))