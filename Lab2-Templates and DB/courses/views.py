from django.shortcuts import render
from .models import Course

def course_search(request):
    query = request.GET.get('q')
    course = None
    
    # 1. Get all courses for the dropdown menu
    all_courses = Course.objects.all()
    
    # 2. If a user selected a course and submitted, filter the results
    if query:
        course = Course.objects.prefetch_related('instructors', 'students').filter(name__iexact=query).first()
        
    return render(request, 'search.html', {
        'course': course, 
        'all_courses': all_courses,
        'selected_query': query # To keep the selection visible
    })