# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse
from storyteller.models import Place

def index(request):
    place_list = Place.objects.all()
    output = ', '.join([p.name for p in place_list])
    return HttpResponse(output)

def place(request, place_id):
    return HttpResponse("You're looking at place %s." % place_id)