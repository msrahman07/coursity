from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from courses.models import Course
from .models import Discussion
from .forms import DiscussionForm
from django.utils import timezone
# Create your views here.
@login_required
def index(request):
    user = request.user
    courses = user.course_set.all()
    context = {
        'courses': courses
    }
    return render(request, "mycourses/index.html", context)

@login_required
def discussion(request, course_id):
    course = Course.objects.get(id=course_id)
    if(request.method=='POST'):
        form = DiscussionForm(request.POST)
        if form.is_valid():
            # form.save()
            topic = form.cleaned_data['topic']
            text = form.cleaned_data['text']
            discussion = Discussion.objects.create(topic=topic, text=text, pub_date=timezone.now(), user=request.user, course=course)
            discussion.save()
    
    discussions = course.discussion_set.all()
    context = {
        'discussions': discussions,
        'course': course
    }
    return render(request, 'mycourses/discussion.html', context)

@login_required
def discussion_detail(request,course_id, disc_id):
    disc = get_object_or_404(Discussion, id=disc_id)
    if(request.method=='POST' and request.user == disc.user):
        disc.delete()
        return discussion(request, course_id)
    else:
        return render(request, 'mycourses/discussion_detail.html', {'disc':disc})
