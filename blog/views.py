from django.shortcuts import render
from rest_framework.views import  APIView
from rest_framework.response import  Response
from rest_framework import  status
from .models import Post,Comment
from .serializers import PostSerializer, CommentSerializer


#3
class posts (APIView):

    def get (self, request):
        posts = Post.objects.all()
        seri = PostSerializer(posts , many = True) #TODO
        return Response(seri.data)

#4  #5
class post (APIView):

    def post (self):
        pass

    def get (self, request):
        pass

#6
class comments (APIView):

    def get (self, request):
        pass


#7
class comment (APIView):

    def post (self):
        pass






