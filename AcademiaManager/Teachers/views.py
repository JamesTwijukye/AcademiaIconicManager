from django.shortcuts import render,redirect,get_object_or_404
from .models import Teacher
from .teacherForm import TeacherForm


# Create your views here.
def allTeachers(request):
    teachers= Teacher.objects.all()
    return render(request,"Teachers/AllTeachers.html",{'teachers':teachers})

def singleTeacher(request,teacher_id):
    teacher= get_object_or_404(Teacher,pk=teacher_id)
    return render(request,"Teachers/SingleTeacher.html",{'teacher':teacher})

def createTeacher(request):
    if request.method =='POST':
        form = TeacherForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_teachers')
        else:
            return render(request,'Teachers/AddTeacher.html',{'form':form})
    else:
        form = TeacherForm()
        return render(request,'Teachers/AddTeacher.html',{'form':form})

def editTeacher(request,pk):
    teacherToEdit = get_object_or_404(Teacher,pk=pk)
    if request.method =='POST':
        form = TeacherForm(request.POST,request.FILES,instance=teacherToEdit)
        if form.is_valid():
            form.save()
            return redirect('single_teacher', pk=teacherToEdit.pk)
    else:
        form = TeacherForm(instance=teacherToEdit)

        return render(request,'Teachers/teacherForm.html',{"form":form})

def deleteTeacher(request,pk):
    teacherToDelete = get_object_or_404(Teacher,pk=pk)
    if request.method=='POST':
        teacherToDelete.delete()
        return redirect('all_teachers')
    else:
        return render(request,'Teachers/DeleteTeacher.html',{'teacher': teacherToDelete})
