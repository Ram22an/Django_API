from rest_framework import serializers
from students.models import Student
from employees.models import Employee
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=['id','emp_id','emp_name','designation']
        read_only_field=['id']


# | `Meta` Option      | Description                                                |
# | ------------------ | ---------------------------------------------------------- |
# | `model`            | Tells which Django model to use                            |
# | `fields`           | List of fields to include in the serializer                |
# | `exclude`          | (Alternative to `fields`) Fields to leave out              |
# | `read_only_fields` | Fields that should not be written to                       |
# | `extra_kwargs`     | Extra field-level settings like required, validators, etc. |
# | `depth`            | For nested relationships                                   |



