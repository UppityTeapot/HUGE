from django.db import models

# Create your models here.

class Object(models.Model):
    name = models.CharField("Name of the object", max_length=30)
    description = models.TextField("The description that will be given when the object is interacted with"max_length=30)
    grabbable = models.BooleanField("Whether this object can be picked up")
    

class Room(models.Model):
    name = models.CharField("Name of the room", max_length=30)
    description = models.TextField("The description that will be given when the object is interacted with"max_length=30)
    # exit_north
    # exit_south
    # exit_east
    # exit_west