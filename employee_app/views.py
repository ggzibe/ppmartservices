from employee_app.models import EmployeeRole, Employee, EmployeeLog
from employee_app.serializers import EmployeeRoleSerializer, EmployeeSerializer, EmployeeReadOnlySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class EmployeeRoleListView(APIView):
    def get(self, request, format=None):
        try:
            queryset = EmployeeRole.objects().all()
            serializer = EmployeeRoleSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception:
            raise Http404

    def post(self, request, format=None):
        serializer = EmployeeRoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeRoleDetailView(APIView):
    def get(self, request, pk, format=None):
        try:
            role = EmployeeRole.objects.get(pk=pk)
            serializer = EmployeeRoleSerializer(role)
            return Response(serializer.data)
        except Exception:
            raise Http404

    def delete(self, request, pk, format=None):
        role = EmployeeRole.objects.get(pk=pk)
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EmployeeListView(APIView):
    def get(self, request, format=None):
        try:
            queryset = Employee.objects().all()
            serializer = EmployeeReadOnlySerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception:
            raise Http404

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetailView(APIView):
    def get(self, request, pk, format=None):
        try:
            employee = Employee.objects.get(pk=pk)
            serializer = EmployeeReadOnlySerializer(employee)
            return Response(serializer.data)
        except Exception:
            raise Http404

    def put(self, request, pk, format=None):
        employee = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        employee = Employee.objects.get(pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
