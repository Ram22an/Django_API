from django.shortcuts import get_object_or_404
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET','POST','PUT','DELETE'])
def studentView(request,student_id):
    # student=get_object_or_404(Student,student_id=student_id)
    # StudentJson={
    #     'student_id':student.student_id,
    #     'name':student.name,
    #     'branch':student.branch
    # }
    # return JsonResponse(StudentJson)

    # students=Student.objects.all()
    # Student_List=list(students.values())
    # to send any data in json format
    # return JsonResponse(Student_List, safe=False)


    # Serializers are used to convert complex data types, like querysets and model instances, into native Python datatypes that can then be easily rendered into JSON, XML or other content types.
    students=get_object_or_404(Student,student_id=student_id)
    if request.method=='GET':
        serializer=StudentSerializer(students)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='PUT':
        serializer=StudentSerializer(students,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        students.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def studentViewAll(request):
    if request.method=='GET':
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

