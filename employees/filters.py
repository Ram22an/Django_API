import django_filters
from .models import Employee


class EmployeeFilter(django_filters.FilterSet):
    # iexact is used to ge the exact field
    designation=django_filters.CharFilter(field_name='designation',lookup_expr='iexact')
    
    # icontains is used to check if any string is present in field
    EmpName=django_filters.CharFilter(field_name='emp_name',lookup_expr='icontains')
    
    # RangeFilter is used to get any field in range and it only work on integer field
    ID=django_filters.RangeFilter(field_name='id')
    
    id_min=django_filters.CharFilter(method='filter_by_id_range',label='From EMP_ID')
    id_max=django_filters.CharFilter(method='filter_by_id_range',label='To EMP_ID')
    class Meta:
        model=Employee
        fields=['designation','EmpName','ID','id_min','id_max']


    def filter_by_id_range(self,queryset,name,value):
        # queryset: The current list of employees.
        # name: The name of the filter that was used (either 'id_min' or 'id_max').
        # value: The number the user typed in.
        if name=='id_min':
            # here emp_id is the field in model of employee
            return queryset.filter(emp_id__gte=value)
            # gte: Stands for Greater Than or Equal to (>=).
        elif name=='id_max':
            # lte: Stands for Less Than or Equal to (<=).
            return queryset.filter(emp_id__lte=value)

        return queryset


