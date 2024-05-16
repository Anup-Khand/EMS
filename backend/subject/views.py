from django.shortcuts import render
from .models import subject
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SubjectSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def subject_api(request):
    if request.method == 'GET':
        subid = request.data.get('subid')
        if subid is not None:
            sub = subject.objects.get(pk=subid)
            serializer = SubjectSerializer(sub)
            return Response(serializer.data)
        sub = subject.objects.all()
        serializer = SubjectSerializer(sub, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = SubjectSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data created'})
        return Response(serializer.errors, status=400)
    if request.method == 'PUT':
        subid = request.data.get('subid')
        sub = subject.objects.get(pk=subid)
        serializer = SubjectSerializer(sub, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data updated'})
        return Response(serializer.errors, status=400)
    if request.method == 'DELETE':
        subid = request.data.get('subid')
        sub = subject.objects.get(pk=subid)
        sub.delete()
        return Response({'msg': 'Data deleted'})

