from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import  APIView
from rest_framework.response import  Response
from rest_framework import  status
from .models import Post,Comment
from .serializers import PostSerializer, CommentSerializer


#3
def get_posts(request,blog_id):
    token=request.META.__getitem__('HTTP_X_TOKEN')# count & offset
    blog = Blog.objects.filter(id=blog_id)
    if request.method == 'GET':
        return JsonResponse(data={'status': 0}, safe=False)
    else:
        return JsonResponse(data={'status': -1}, safe=False)


#4  #5
def post(request,blog_id):
    token=request.META.__getitem__('HTTP_X_TOKEN')
    if request.method == 'GET':
        id=request.GET['id']
        return JsonResponse(data={'status': 0}, safe=False) #TODO blog id
    if request.method == 'POST':
        title=request.POST['title']
        summary=request.POST['summary']
        text=request.POST['text']
        return JsonResponse(data={'status': 0}, safe=False)
    else:
        return JsonResponse(data={'status': -1}, safe=False)

#6


#7







