from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Class,Student
from django.contrib.auth import get_user_model


class ClassSerializer(serializers.Serializer):
    class Meta:
        model = Class
        fields = ["class_name"]


# Create a serializer for Student model
class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ["username","password","email"]

class StudentSerializer(serializers.Serializer):
    user = UserSerializer()
    class Meta:
        model = Student
        fields = "__all__"

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        student = Student.objects.create(user=user,**validated_data)
        return student



# create a serializer for the custom user model
class CustomUserSerializer(serializers.Serializer):
    class Meta:
        model = get_user_model()
        fields = ["id","username","phone","password"]
        extra_kwargs = {"password":{"write_only":True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data["username"],
            phone=validated_data["phone"],
            password=validated_data["password"]
        )
        return user