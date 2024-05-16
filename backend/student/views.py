from django.shortcuts import render
from .models import Students
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentsSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request):
    if request.method == 'GET':
        stuid = request.data.get('stuid')
        if stuid is not None:
            stu = Students.objects.get(pk=stuid)
            serializer = StudentsSerializer(stu)
            return Response(serializer.data)
        stu = Students.objects.all()
        serializer = StudentsSerializer(stu, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = StudentsSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data created'})
        return Response(serializer.errors, status=400)
    if request.method == 'PUT':
        stuid = request.data.get('stuid')
        stu = Students.objects.get(pk=stuid)
        serializer = StudentsSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data updated'})
        return Response(serializer.errors, status=400)
    if request.method == 'DELETE':
        stuid = request.data.get('stuid')
        stu = Students.objects.get(pk=stuid)
        stu.delete()
        return Response({'msg': 'Data deleted'})