from django.contrib import admin

from .models import Student, Card, Department, Course

admin.site.register(Student)
admin.site.register(Card)
admin.site.register(Department)
admin.site.register(Course)
