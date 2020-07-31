from django.db import models

from courses.models import Course
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Discussion(models.Model):
    topic = models.CharField(max_length=50)
    text = models.CharField(max_length=5000)
    pub_date = models.DateTimeField('date published')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.topic


class Comment(models.Model):
    text = models.CharField(max_length=3000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)

    def __str__(self):
        return self.text