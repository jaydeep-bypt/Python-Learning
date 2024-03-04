from django.http import Http404, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employee
from .serializer import EmployeeSerializer
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['GET', 'POST'])
def EmployeeDetails(request):
    if request.method == 'GET':
        obj = Employee.objects.all()
        data = {"response": list(obj.values("id", "name"))}
        return JsonResponse(data)

    elif request.method == "POST":
        data = request.data
        obj = Employee(name=data.get("name"))
        obj.save()
        data = {'response': {'id': obj.id, 'name': obj.name}}
        return JsonResponse(data)

class ListEmployee(APIView):
    emp_list = Employee.objects.all()
    paginator = Paginator(emp_list, 3)

    def get(self, request):
        obj = Employee.objects.all()
        serializer_obj = EmployeeSerializer(obj, many=True)
        return Response(serializer_obj.data)

    def post(self, request):
        data = request.data
        serializer_obj = EmployeeSerializer(data=data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)

class UpdateEmployee(APIView):
    def get_object(self, id):
        try:
            obj = Employee.objects.get(id=id)
            return obj
        except Employee.DoesNotExist:
            raise Http404

    def put(self, request, id):
        data = request.data
        obj = self.get_object(id)
        serializer_obj = EmployeeSerializer(obj, data=data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)

    def delete(self, request, id):
        obj = self.get_object(id)
        obj.delete()
        return Response({"response": "Employee is successfully deleted."})
