from .models import Post
from .serializers import PostSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class PostList(APIView):

    def get(self, request, format=None):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, context={"request": request}, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False) 

    def post(self, request, format=None):
       serializer = PostSerializer(data=request.DATA)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)