from rest_framework import serializers
from .models import * 


class EmpSerialilzer(serializers.ModelSerializer):
    class Meta:
        model= Emp
        fields='__all__' 