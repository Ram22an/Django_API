from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def StudentList(reuqest):
    students=[
        {'id':1,
        'name':'John Doe',
        'age':20}
    ]
    # return HttpResponse("this is student list")
    return HttpResponse(students)
