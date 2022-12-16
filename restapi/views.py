from django.contrib.auth.models import User

# class base
# from rest_framework import status, authentication, permissions
# from rest_framework.decorators import api_view, authentication_classes, permission_classes
# from rest_framework.views import APIView

# function base
from rest_framework.decorators import api_view

# Response for class base and function base
from rest_framework.response import Response

from . import models
from .serializers import PostSerializer


# class PostsList(APIView):
#     # authentication_classes = [authentication.TokenAuthentication]
#     # permission_classes = [permissions.IsAuthenticated, isAdminUser]

#     def get(self, request, format=None):
#         # posts = models.Post.objects.filter(user=request.user)
#         posts = models.Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
        
#         titles = [post.title for post in models.Post.objects.all()]
#         # print(titles)
#         return Response(serializer.data)
    
    
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def postsList(request, format=None):    # format for http://127.0.0.1:8000/api.json
    if request.method == 'GET':
        # get all posts
        posts = models.Post.objects.all()
        
        # serialize them
        serializer = PostSerializer(posts, many=True)       # GET: PostSerializer(posts, many=True) with queried posts
        
        # titles = [post.title for post in models.Post.objects.all()]
        # print(titles)
        
        # return rest_framework json
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)      # POST: PostSerializer(data=request.data) with request data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk, format=None):  # format for http://127.0.0.1:8000/api.json
    try:
        post = models.Post.objects.get(id=pk)
    except models.Post.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)    # similer to POST with getting data from the request, but with adding post
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)