from rest_framework.serializers import (
	CharField,
    Serializer,
    RegexField,
    FileField,
    ValidationError,
) 
from django.core.validators import FileExtensionValidator
from webapp.models import *

# class EmployeesSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Employees
# 		fields = "__all__"
class MBTISerializer(Serializer):
    image = FileField(required=True, validators=[FileExtensionValidator(["png"])])
