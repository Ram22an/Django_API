from django.urls import path,include
from . import views
urlpatterns = [
    path('students/',views.studentViewAll,name='studentViewAll'),
    path('students/<str:student_id>/',views.studentView,name='studentView'),
    
    # Class as view
    path('employees/',views.EmployeesClass.as_view()),
    path('employees/<str:emp_id>/',views.EmployeesClassPUT.as_view())
]
