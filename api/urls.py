from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

# | Parameter        | Affects                                | Visible in URL? |
# | ---------------- | -------------------------------------- | --------------- |
# | `'employees'`    | URL path                               | ✅ Yes          |
# | `basename='...'` | Route names (reverse lookups, testing) | ❌ No           |

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


    path('blogs/',views.BlogsView.as_view()),
    path('comments/',views.CommentsView.as_view()),
    
    path('blogs/<int:pk>/',views.BlogsViewPkValue.as_view()),
    path('comments/<int:pk>/',views.CommentsViewPkValue.as_view()),
]
