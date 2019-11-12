from django.shortcuts import render, redirect
from student.forms import StudentForm
from student.models import Student
# Create your views here.
def stud(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = StudentForm()
    return render(request,'index.html',{'form':form})
def show(request):
    employees = Student.objects.all()
    return render(request,"show.html",{'Student':Student})
def edit(request, id):
    employee = Student.objects.get(id=id)
    return render(request,'edit.html', {'Student':Student})
def update(request, id):
    employee = Student.objects.get(id=id)
    form = StudentForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'Student':Student})
def destroy(request, id):
    employee = Student.objects.get(id=id)
    employee.delete()
    return redirect("/show")