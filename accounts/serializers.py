from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    Department = serializers.CharField()
    StudentID = serializers.CharField()

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'phone': self.validated_data.get('phone', ''),
            'birthday': self.validated_data.get('birthday', ''),
            'address1': self.validated_data.get('address1', ''),
            'address2': self.validated_data.get('address2', ''),
            'address3': self.validated_data.get('address3', ''),
            'usertype': self.validated_data.get('usertype', ''),
            'profile': self.validated_data.get('profile', ''),
        }