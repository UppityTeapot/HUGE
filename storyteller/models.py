from django.db import models

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=30)
    # broken exit_north = models.OneToOneField('self', to_field='exit_south')
    # broken exit_south = models.OneToOneField('self', to_field='exit_south')
    # broken exit_east = models.OneToOneField('self', to_field='exit_west')
    # broken exit_west = models.OneToOneField('self', to_field='exit_east')
    
    def __unicode__(self):
        return self.name
        return self.description

class Thing(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=30)
    location = models.ForeignKey(Place)
    grabbable = models.BooleanField("Can we pick this up?")
    
    def __unicode__(self):
        return self.name
        return self.description