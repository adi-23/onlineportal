from .views import StudentRegisterAPI,EducatorRegisterAPI,StudentLoginAPI,EducatorLoginAPI,CreateCourse,EnrolledAPI
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('student/register/', StudentRegisterAPI.as_view()),
    path('educator/register/',EducatorRegisterAPI.as_view()),
    path('student/login/',StudentLoginAPI.as_view()),
    path('educator/login/',EducatorLoginAPI.as_view()),
    path('course/',CreateCourse.as_view()),#gives list of courses
    path('course/<int:id>',CreateCourse.as_view()),# id course id
    path('enrolled/',EnrolledAPI.as_view()),
    path('enrolled/course/<int:id>',EnrolledAPI.as_view())# please give id as course id
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)