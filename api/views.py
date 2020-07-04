from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ListsSerializer
from .models import Lists

@api_view(['GET'])
def listAll(request):
    list = Lists.objects.all()
    serializer = ListsSerializer(list,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listDetail(request,pk):
    list = Lists.objects.get(id=pk)
    serializer = ListsSerializer(list,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def listCreate(request):
    serializer = ListsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def listUpdate(request,pk):
    list = Lists.objects.get(id=pk)
    serialize = ListsSerializer(instance=list,data=request.data)
    if serialize.is_valid():
        serialize.save()
    return Response(serialize.data)

@api_view(['DELETE'])
def listDelete(request,pk):
    list = Lists.objects.get(id=pk)
    list.delete()
    return Response('success delete')
