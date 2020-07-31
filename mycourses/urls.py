from django.urls import path
from . import views

app_name = 'mycourses'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_id>/discussion/', views.discussion, name='discussion'),
    path('<int:course_id>/discussion/<int:disc_id>/', views.discussion_detail, name='discussion_detail')

]