from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    user = request.user
    courses = user.course_set.all()
    context = {
        'courses': courses
    }
    return render(request, "mycourses/index.html", context)