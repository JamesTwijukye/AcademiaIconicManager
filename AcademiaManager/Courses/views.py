
# Create your views here.

from django.shortcuts import render,redirect,get_object_or_404
from .models import Course
from .courseform import CourseForm


# Create your views here.

def CourseDetails(request,code):
    course = get_object_or_404(Course,pk=code)
    teacher= Course.teacher
    students=Course.students.all()
    return render(request,'Courses/courseDetails.html',
                  {'course':course,
                   'teacher':teacher,
                   'students':students})

def AllCourses(request):
    courses = Course.objects.all()  
    return render(request, 'Courses/AllCourses.html', {'Courses': courses})

   

def SingleCourse(request,code):
    course= get_object_or_404(Course,pk=code)
    return render(request,'Courses/SingleCourse.html',{'Course':course})

def createCourse(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_courses') 
        else:
            return render(request, 'Courses/AddCourse.html', {'form': form})
    else:
        form = CourseForm()
        return render(request, 'Courses/AddCourse.html', {'form': form})

def editStudent(request,pk):
    CourseToEdit = get_object_or_404(Course,pk=pk)
    if request.method=='POST':
        form = CourseForm(request.POST,request.FILES,instance=CourseToEdit)
        if form.is_valid():
            form.save()
            return redirect('singleCourse.html',pk=CourseToEdit.pk)
    else:
        form =CourseForm(instance=CourseToEdit)
        return render(request,'Courses/CourseFormPage.html',{'form':form})
 


def deleteStudent(request,pk):
    CourseToDelete = get_object_or_404(Course,pk=pk)
    if request.method=='POST':
        CourseToDelete.delete()
        return redirect('all_courses') 
    else:
        return render(request,'Courses/DeleteCourse.html',{'course':CourseToDelete})
 





