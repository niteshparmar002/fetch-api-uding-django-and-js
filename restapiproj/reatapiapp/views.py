from .models import employee
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import employeeSerializer


class employeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = employee.objects.all()
    serializer_class = employeeSerializer