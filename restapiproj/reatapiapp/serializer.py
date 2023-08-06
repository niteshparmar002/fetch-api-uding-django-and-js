from rest_framework import serializers
from .models import employee
# from rest_framework import employee

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = ['firstname', 'lastname']
        # fields = "__all__"   for all fields of table
