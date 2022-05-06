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

@api_view(['GET'])
def music_detail(request, pk):
   try:
    music=Music.objects.get(pk=pk)
    serializer=Musicserializer(music)
    return Response(serializer.data)
    
   except Music.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

