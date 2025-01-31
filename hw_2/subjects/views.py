from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Course

def courses_list(request):
    courses = list(Course.objects.values())
    return JsonResponse(courses, safe=False)

def course_detail(request, id):
    try:
        course = Course.objects.get(id=id)
        return JsonResponse({
            "id": course.id,
            "title": course.title,
            "text": course.text,
            "author": course.author
        })
    except Course.DoesNotExist:
        return JsonResponse({"error": "Course not found"}, status=404)
