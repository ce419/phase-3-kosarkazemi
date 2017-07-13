from rest_framework.views import  APIView
from rest_framework.response import  Response
from django.views import generic
from rest_framework import  status
from .models import User, Blog
# from .serializers import UserSerializer
from django.http import Http404
from django.http import JsonResponse

#1
class register (generic.FormView):
    model = User
    def post(self, request):

        # serializer = UserSerializer(data = request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=111)
        # return Response(serializer.errors, status=100)
        newUser = request.data
        # redirect_field_name = 'redirect_to'



#2
class login (APIView):



    # if request.method == 'POST':
    #     # create a form instance and populate it with data from the request:
    #     print(request.POST)
    #     form = LoginForm(data=request.POST)
    #     # check whether it's valid:
    #     if form.is_valid():
    #         username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password')
    #         user = authenticate(username=username, password=password)
    #         login(request, user)
    #         token = token_generator.make_token(user)
    #         bu = BlogUser.objects.get(username=username)
    #         bu.token = token
    #         bu.save()
    #         return JsonResponse(data={'status': 0 , 'token': token}, safe=False)
    #     else:
    #         return JsonResponse(data={'status': -1 , message': form.errors["__all__"]}, safe=False)

    def post (self):
        pass

