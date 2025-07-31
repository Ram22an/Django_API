from django.shortcuts import get_object_or_404
from students.models import Student
from employees.models import Employee
from .serializers import StudentSerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins,generics,viewsets
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



# these two classes are without mixins
# class EmployeesClass(APIView):
#     def get(self,request):
#         employees=Employee.objects.all()
#         EmployeeSer=EmployeeSerializer(employees,many=True)
#         return Response(EmployeeSer.data,status=status.HTTP_200_OK)
#     def post(self,request):
#         EmployeeSer=EmployeeSerializer(data=request.data)
#         if EmployeeSer.is_valid():
#             EmployeeSer.save()
#             return Response(EmployeeSer.data,status=status.HTTP_201_CREATED)
#         return Response(EmployeeSer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
    

# class EmployeesClassID(APIView):
#     def get_object(self,id):
#         return get_object_or_404(Employee,id=id)
#     def get(self,request,id):
#         employees=self.get_object(id)
#         EmployeeSer=EmployeeSerializer(employees)
#         return Response(EmployeeSer.data,status=status.HTTP_200_OK)
#     def put(self,request,id):
#         employee= self.get_object(id)
#         EmployeeSer=EmployeeSerializer(employee,data=request.data)
#         if EmployeeSer.is_valid():
#             EmployeeSer.save()
#             return Response(EmployeeSer.data,status=status.HTTP_202_ACCEPTED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#     def delete(self,request,id):
#         employee=self.get_object(id)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




# these are mixins based classes
# class EmployeesClass(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer

#     def get(self,request):
#         return self.list(request)
    
#     def post(self,request):
#         return self.create(request)

# class EmployeesClassID(mixins.DestroyModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     lookup_field='id'
#     def get(self,request,id):
#         return self.retrieve(request,id)
#     def put(self,request,id):
#         return self.update(request,id)
#     def delete(self,request,id):
#         return self.destroy(request,id)


# Generic based classes
# class EmployeesClass(generics.ListCreateAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer

# class EmployeesClassID(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     lookup_field='id'



# Generic based classes with viewsets
# class EmployeeViewSet(viewsets.ViewSet):
#     def list(self,request):
#         queryset=Employee.objects.all()
#         serializer=EmployeeSerializer(queryset,many=True)
#         return Response(serializer.data)
#     def create(self,request):
#         serializer=EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def retrieve(self,request,pk=None):
#         employee=get_object_or_404(Employee,pk=pk)
#         serializer=EmployeeSerializer(employee)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     def update(self,request,pk=None):
#         employee=get_object_or_404(Employee,pk=pk)
#         serializer=EmployeeSerializer(employee,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors)
#     def delete(self,request,pk=None):
#         employee=get_object_or_404(Employee,pk=pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# class using model view set
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer



from blogs.models import Blogs,Comments
from blogs.serializers import BlogSerializer,CommentSerializer


class BlogsView(generics.ListCreateAPIView):
    queryset=Blogs.objects.all()
    serializer_class=BlogSerializer



class CommentsView(generics.ListCreateAPIView):
    queryset=Comments.objects.all()
    serializer_class=CommentSerializer



class BlogsViewPkValue(generics.RetrieveUpdateDestroyAPIView):
    queryset=Blogs.objects.all()
    serializer_class=BlogSerializer
    lookup_field='pk'


class CommentsViewPkValue(generics.RetrieveUpdateDestroyAPIView):
    queryset=Comments.objects.all()
    serializer_class=CommentSerializer
    lookup_field='pk'




