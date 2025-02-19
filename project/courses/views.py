from django.shortcuts import render, redirect
from .forms import StudentForm

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page or another page after submission
    else:
        form = StudentForm()
    
    return render(request, 'student_create.html', {'form': form})


def home(request):
    return render(request, 'home.html')  # Ensure 'home.html' exists in the templates folder

def courses(request):
    return render(request, 'courses/courses.html')  # Add this function
def form_google(request):
    return render(request, 'form_google.html')  # Add this function