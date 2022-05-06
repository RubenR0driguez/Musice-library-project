from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Music
from .serializers import Musicserializer
# Create your views here.

@api_view(['GET','POST'])
def music_list(request):

   if request.method == 'GET':
    music = Music.objects.all()
    serializer = Musicserializer(music, many=True)
    return Response(serializer.data)


   elif request.method == 'POST':
      serializer = Musicserializer(data=request.data)
      if serializer.is_valid()==True:
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      else:
          Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def music_detail(request, pk):
   music = get_object_or_404(Music, pk=pk)
   if request.method == 'GET':
    serializer = Musicserializer(music)
    return Response(serializer.data)
   elif request.method =='PUT':
     music = get_object_or_404(Music,pk=pk)
     serializer = Musicserializer(music, data=request.data)
     serializer.is_valid(raise_exception=True)
     serializer.save()
     return Response(serializer.data)
   elif request.method == 'DELETE':
      music.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
