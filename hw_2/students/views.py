from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Student

def students_list(request):
    students = list(Student.objects.values())
    return JsonResponse(students, safe=False)

def student_detail(request, id):
    try:
        student = Student.objects.get(id=id)
        return JsonResponse({
            "id": student.id,
            "name": student.name,
            "surname": student.surname,
            "major": student.major,
            "year_of_study": student.year_of_study,
            "faculty": student.faculty
        })
    except Student.DoesNotExist:
        return JsonResponse({"error": "Student not found"}, status=404)
