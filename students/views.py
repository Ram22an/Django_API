from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def StudentList(reuqest):
    return HttpResponse("this is student list")
