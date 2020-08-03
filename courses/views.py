from django.shortcuts import render, redirect, reverse
from .models import Course
# Create your views here.
from django.contrib.auth.decorators import login_required

def index(request, newContext={}):
    if(request.user.is_authenticated):
        print(request.user.id)
    else:
        print("NO USER LOGGED IN")
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    context.update(newContext)
    return render(request, 'courses/index.html', context)

@login_required
def enroll(request, course_id):
    success_msg = ""
    if(request.method == 'POST'):
        course = Course.objects.get(id=course_id)
        print(request.user)
        if(course not in request.user.course_set.all()):
            course.users.add(request.user)
            course.save()
            success_msg = "Enrolled in "+course.name+" successfully!!"
        else:
            success_msg = "Course already enrolled"

    return index(request, {'success_msg':success_msg})
    # if(request.user.is_authenticated):
