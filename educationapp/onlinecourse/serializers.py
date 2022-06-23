from attr import field
from .models import Student,Educator,Course,Tutorial,Enrolled
from rest_framework import serializers
from django.contrib.auth.models import User
#from .models import Student
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

#Student Serializer
class StudentSerializer(serializers.ModelSerializer):
    student=UserSerializer(many=False,)
    class Meta:
        model=Student
        fields=('student',)

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

class EducatorSerializer(serializers.ModelSerializer):
    educator=UserSerializer(many=False,)
    class Meta:
        model=Educator
        fields=('educator',)

class CourseSerializer(serializers.ModelSerializer):
    created_by=EducatorSerializer(many=False,)
    images=serializers.ImageField(required=False)

    class Meta:
        model=Course
        fields=('name','description','created_by','images')

class EnrolledSerializer(serializers.ModelSerializer):
    student=StudentSerializer(many=False,)
    course=CourseSerializer(many=False,)
    class Meta:
        model=Enrolled
        fields=('student','course')