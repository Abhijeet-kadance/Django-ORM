from django.shortcuts import render
from django.http import HttpResponse
from .models import Department, Professor, Student, Enrollment, Course, Classroom
from .forms import RatingForm

# Create your views here.
def orm_test(request):
    #dep = Department.objects.create(name="Computer")
    # = Professor.oprofbjects.create(name="Arav Mehta",department=dep, hire_date="2020-01-01")
    #dep.head = prof
    #dep.save()
    
    # departments = Department.objects.select_related('head')
    
    # for dep in departments:
    #     print(dep.name,dep.head.name)
        
    # dep = Department.objects.get(name="Chemical")
    # print(dep.head.name)
    # prof = Professor.objects.get(name="Dr. Singh")
    # print(prof.headed_department.name)
    # new_dep = Department.objects.create('IT')
    # new_dep.save()
    # dep = Department.objects.get(name='IT')
    # new = Professor.objects.create(name="Sushma Mehta",department=dep, hire_date="2020-01-01")
    # new.save()
    # print(dep.head)
    
    # department = Department.objects.all()
    # print(department.values_list())
    # print(department.values())
    # departments = list(department.values())
    
    # dep = Department.objects.get(name='IT')
      
    # prof = Professor.objects.get(name="Sushma Mehta")
    # print(new.head)
    # if hasattr(prof,'headed_department'):
    #     print("This professor is a head of department")
    # else:
    #     print("Not a HOD")
    

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Form errors:", form.errors)
            return render(request, 'core/index.html', {'form': form})
    
    # if request.method == 'POST':
    #     form = RatingForm(request.POST or None)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #     else:
    #         return render(request,'core/index.html',{'form':form})
    
    # if request.method == 'POST':
    #     form = RestaurentForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     else:
    #         print("Form errors:", form.errors)
    #         return render(request, 'core/index.html', {'form': form})
    
    return render(request, 'core/index.html', {'form': RatingForm()})