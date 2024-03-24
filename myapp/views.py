from django.shortcuts import render, redirect
from .models import Student, Course

def students(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            email=request.POST['email']
        )
        return redirect('students')

    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})

# Courses view
def courses(request):
    if request.method == 'POST':
        Course.objects.create(
            name=request.POST['name'],
            description=request.POST['description']
        )
        return redirect('courses')

    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

def details(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        course_id = request.POST['course']
        course = Course.objects.get(id=course_id)
        student.courses.add(course)
        return redirect('details', student_id=student_id)

    not_registered_courses = Course.objects.exclude(students=student)
    return render(request, 'details.html', {
        'student': student,
        'notRegisteredCourses': not_registered_courses
    })
