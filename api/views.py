from django.shortcuts import get_object_or_404
from students.models import Student
from employees.models import Employee
from .serializers import StudentSerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
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




class EmployeesClass(APIView):
    def get(self,request):
        employees=Employee.objects.all()
        EmployeeSer=EmployeeSerializer(employees,many=True)
        return Response(EmployeeSer.data,status=status.HTTP_200_OK)
    def post(self,request):
        EmployeeSer=EmployeeSerializer(data=request.data)
        if EmployeeSer.is_valid():
            EmployeeSer.save()
            return Response(EmployeeSer.data,status=status.HTTP_201_CREATED)
        return Response(EmployeeSer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
    

class EmployeesClassPUT(APIView):
    def get(self,request,id):
        employees=get_object_or_404(Employee,id=id)
        EmployeeSer=EmployeeSerializer(employees)
        return Response(EmployeeSer.data,status=status.HTTP_200_OK)
    def put(self,request,id):
        employee=get_object_or_404(Employee,id=id)
        EmployeeSer=EmployeeSerializer(employee,data=request.data)
        if EmployeeSer.is_valid():
            EmployeeSer.save()
            return Response(EmployeeSer.data,status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)



