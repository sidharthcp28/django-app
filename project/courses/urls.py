from django.urls import path
from . import views

# URL patterns for the courses app
urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('student/create/', views.student_create, name='student_create'),  # Student creation form
    path('courses/', views.courses, name='courses'),  # Courses page
    path('course/create/', views.form_google, name='form_google'),  #  form
]
