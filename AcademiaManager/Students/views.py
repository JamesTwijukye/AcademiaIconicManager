from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from .studentForm import StudentForm
from django.http import HttpResponse


# Create your views here.

def homepage(request):
    return HttpResponse("Welcome to Academia Manager")


def AllStudents(request):
    students = Student.objects.all()  # Query all students from DB
    return render(request, 'Students/AllStudents.html', {'students': students})

   

def SingleStudents(request,student_id):
    student= get_object_or_404(Student,pk=student_id)
    return render(request,'Students/SingleStudent.html',{'student':student})

def createStudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_students') 
        else:
            return render(request, 'Students/Addstudent.html', {'form': form})
    else:
        form = StudentForm()
        return render(request, 'Students/Addstudent.html', {'form': form})

def editStudent(request,pk):
    studentToEdit = get_object_or_404(Student,pk=pk)
    if request.method=='POST':
        form = StudentForm(request.POST,request.FILES,instance=studentToEdit)
        if form.is_valid():
            form.save()
            return redirect('singleStudent.html',pk=studentToEdit.pk)
    else:
        form =StudentForm(instance=studentToEdit)
        return render(request,'Students/studentFormPage.html',{'form':form})
 


def deleteStudent(request,pk):
    studentToDelete = get_object_or_404(Student,pk=pk)
    if request.method=='POST':
        studentToDelete.delete()
        return redirect('all_students') 
    else:
        return render(request,'Students/DeleteStudent.html',{'student':studentToDelete})
 





