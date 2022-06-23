import pkg_resources
from rest_framework import generics,permissions
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from knox.models import AuthToken
from rest_framework.views import APIView
from .serializers import EnrolledSerializer, UserSerializer, RegisterSerializer,StudentSerializer,EducatorSerializer,CourseSerializer
from django.contrib.auth.models import User
from .models import Course, Student,Educator,Enrolled
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
#from rest_framework.renderers import JsonRenderer

# Register API for Student
class StudentRegisterAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        studentobj=Student.objects.create(student=user)
        studentobj.save()        
        return Response({
        "student": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

#class based register API for educator
class EducatorRegisterAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        educatorobj=Educator.objects.create(educator=user)
        educatorobj.save()        
        return Response({
        "educator": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
#Login API for Student

class StudentLoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=False)
        user = serializer.validated_data['user']
        if user:
            s=Student.objects.get(student=user)
            if s:
                login(request, user)
                return super(StudentLoginAPI, self).post(request, format=None)
            else:
                return Response({"error": "Details are incorrect"})
        else:
            return Response({"error": "No user exsists"})

#Login API for Educator 
class EducatorLoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=False)
        user = serializer.validated_data['user']
        if user:
            e=Educator.objects.get(educator=user)
            if e:
                login(request, user)
                return super(EducatorLoginAPI, self).post(request, format=None)
            else:
                return Response({"error": "Details are incorrect"})
        else:
            return Response({"error": "No user exsists"})

#Create a Course
class CreateCourse(APIView):
    permission_classes=[AllowAny,]
    parser_classes=[MultiPartParser, FormParser,JSONParser]
    query_set=Course.objects.all()
    #to post a course by user by id
    def post(self,request,format=None):
        data=request.data
        print(data)
        name=data.get('name')
        description=data.get('description')
        id=data.get('id')
        image=data.get('images')
        user=User.objects.get(pk=id)
        e=Educator.objects.get(pk=id)
        print(e)
        
        course=Course.objects.create(name=name,description=description,created_by=e,images=image)
        course.save()
        c=CourseSerializer(course)
        
        return Response(c.data)
    #gives all courses to users
    def get(self,request, format=None):
        courses=Course.objects.all()
        c=CourseSerializer(courses,many=True)
        return Response(c.data)
    #gives a specific course by id
    def get(self,request,id=None):
        course=Course.objects.get(pk=id)
        c=CourseSerializer(course)
        return Response(c.data)

class EnrolledAPI(APIView):
    permission_classes=[AllowAny,]
    parser_classes=[JSONParser]
    query_set=Enrolled.objects.all()
    #API to enroll student based on course id and student id
    def post(self,request,format=None):
        data=request.data
        id=data.get('id')#student id
        cid=data.get('cid') #course id
        student=Student.objects.get(pk=id)
        course=Course.objects.get(pk=cid)
        enroll=Enrolled.objects.create(student=student,course=course)
        enroll.save()
        enrollobj=EnrolledSerializer(enroll)
        return Response(enrollobj.data)
    #API for students for given course
    def get(self,request,id=None):
        course=Course.objects.get(pk=id)
        enrl=Enrolled.objects.filter(course=course)
        students=[]
        for j in enrl:
            students=students+[j.student]
        s=StudentSerializer(students,many=True)
        return Response(s.data)