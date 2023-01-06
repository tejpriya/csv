from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .resources import cvResource
from tablib import Dataset
from django.utils.datastructures import MultiValueDictKeyError
from .models import cv

def export(request):
    person_resource = cvResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response
def input_file(request):
    return render(request,'input.html')
def simple_upload(request):
    # print("simple", request.FILES['C:/Users/COSAI02/Djangoproject/csv1/persons.xls']);
    print (request.method,request.FILES)
    if request.method == 'POST':
        person_resource = cvResource()
        dataset = Dataset(header=['name', 	'age'])
        new_persons = request.FILES['persons']
        print ("new_persons")
        if not new_persons.name.endswith('xls'):
            messages.info(request,'wrong format')
            return render(request,'upload.html')
        imported_data = dataset.load(new_persons.read(),format='xls')
        #print(imported_data)
        for data in imported_data:
        	
            value = cv(
        		data[0],
        		data[1])
            value.save()       
        
       

    return render(request, 'upload.html')
    
