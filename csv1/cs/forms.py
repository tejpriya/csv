from django import forms
from .models import cv

class PersonData(forms.Form):
	class meta:
		model = cv
		fields = '__all__'