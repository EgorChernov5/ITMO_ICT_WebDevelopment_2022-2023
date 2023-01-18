from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Guest, Employee


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('phone_guest', 'passport_guest')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('hotel_empl', 'phone_employee', 'position_employee')
        depth = 1


class MyUserSerializer(serializers.ModelSerializer):
    user_guest = GuestSerializer(required=False)
    user_employee = EmployeeSerializer(required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'user_guest', 'user_employee')
