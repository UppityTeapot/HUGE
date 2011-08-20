from storyteller.models import Thing
from storyteller.models import Place
from django.contrib import admin

class ThingInline(admin.TabularInline):
    model = Thing
    extra = 1

class PlaceAdmin(admin.ModelAdmin):
    inlines = [ThingInline]

admin.site.register(Place, PlaceAdmin)