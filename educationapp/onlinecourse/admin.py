from django.contrib import admin
from .models import Student,Educator,Tutorial,Course,Enrolled
# Register your models here.
admin.site.register(Student)
admin.site.register(Educator)
admin.site.register(Course)
admin.site.register(Tutorial)
admin.site.register(Enrolled)