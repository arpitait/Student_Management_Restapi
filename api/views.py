from rest_framework import generics
from .models import Class,Student
from .serializers import ClassSerializer,StudentSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


# create a form view to add a class
class ClassView(generics.CreateAPIView):
    queryset = Class
    serializer_class = ClassSerializer


# Create a view to register a student
class StudentRegistration(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# Create Login for Student
class StudentLogin(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data["token"])
        student = Student.objects.get(user=token.user)
        if not student.status:
            return Response({"error":"Student is not activated yet"},status=status.HTTP_401_UNAUTHORIZED)
        return response


# Create a view to update the student's profile
class StudentProfileUpdate(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.student



