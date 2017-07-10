from rest_framework import serializers
from .models import User,Blog



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('std_num','password' , 'first_name',  'last_name', 'email') #TODO mmm