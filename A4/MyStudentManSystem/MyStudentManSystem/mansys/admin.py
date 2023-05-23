from django.contrib import admin
from .models import Student,Faculty,Classroom,Department,Course,Instructor,Section,Takes,Advisor,Prereq,Time_slot

# Register your models here.
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Classroom)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Section)
admin.site.register(Takes)
admin.site.register(Advisor)
admin.site.register(Prereq)
admin.site.register(Time_slot)

