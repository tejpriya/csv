from cs import views
from django.contrib import admin
from django.urls import path,include
urlpatterns=[
        path('inp/',views.input_file),
        path('',views.simple_upload),
        path('export/',views.export),
]