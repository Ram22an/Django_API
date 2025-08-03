import django_filters
from .models import Employee


class EmployeeFilter(django_filters.FilterSet):
    # iexact is used to ge the exact field
    designation=django_filters.CharFilter(field_name='designation',lookup_expr='iexact')
    
    # icontains is used to check if any string is present in field
    EmpName=django_filters.CharFilter(field_name='emp_name',lookup_expr='icontains')
    
    # RangeFilter is used to get any field in range
    ID=django_filters.RangeFilter(field_name='id')
    
    class Meta:
        model=Employee
        fields=['designation','EmpName','ID']





