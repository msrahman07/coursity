from django.shortcuts import render
from .models import Course
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'courses/index.html', context)