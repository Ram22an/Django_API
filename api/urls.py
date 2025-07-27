from django.urls import path,include
from . import views
urlpatterns = [
    path('students/<str:student_id>/',views.studentView,name='studentView'),
]
