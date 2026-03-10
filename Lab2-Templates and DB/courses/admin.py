from django.contrib import admin
from .models import Course
from students.models import Student

# Inline for Students (One-to-Many: One Course has many Students)
class StudentInline(admin.TabularInline):
    model = Student
    extra = 1  # Number of empty rows to show

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [StudentInline]
    # This allows you to select Instructors in the same UI
    filter_horizontal = ('instructors',)