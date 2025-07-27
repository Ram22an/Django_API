from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def studentView(request):
    Student={
        'Id':1,
        'name':'raman',
        'class':'Computer Science'
    }
    return JsonResponse(Student)
