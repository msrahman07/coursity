from django.shortcuts import render
from django.http import HttpResponse

from .models import Student
# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the students page.")
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, "students/index.html", context)