from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Course(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.code