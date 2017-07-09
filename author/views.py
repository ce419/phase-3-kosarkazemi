from rest_framework.views import  APIView
from rest_framework.response import  Response
from rest_framework import  status
from .models import User, Blog
from .serializers import UserSerializer
from django.http import Http404

#1
class register (APIView):

    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=111)
        return Response(serializer.errors, status=-100)


#2
class login (APIView):

    def post (self):
        pass

