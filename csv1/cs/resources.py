#from cs import resources
from import_export import resources
from cs.models import cv

class cvResource(resources.ModelResource):
    class Meta:
        model = cv
       