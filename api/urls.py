from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('employees',views.EmployeeViewSet,basename='employee')


urlpatterns = [
    path('students/',views.studentViewAll,name='studentViewAll'),
    path('students/<str:student_id>/',views.studentView,name='studentView'),
    
    # Class as view
    # path('employeesall/',views.EmployeesClass.as_view()),
    # path('employees/<int:id>/',views.EmployeesClassID.as_view())

    # generic based classes
    path('',include(router.urls)),
]
