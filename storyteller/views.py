# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from storyteller.models import Place

def index(request):
    place_list = Place.objects.all().order_by('-    name')
    return render_to_response('place/index.html', {'place_list': place_list})

def place(request, place_id):
    return HttpResponse("You're looking at place %s." % place_id)

def detail(request, place_id):
    try:
        p = Place.objects.get(pk=poll_id)
    except Place.DoesNotExist:
        raise Http404
    return render_to_response('polls/detail.html', {'poll': p})