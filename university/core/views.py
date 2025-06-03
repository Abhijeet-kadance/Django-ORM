from django.shortcuts import render
from django.http import HttpResponse
from .models import Department, Professor, Student, Enrollment, Course, Classroom
from .forms import RestaurentForm
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
    

    # if request.method == 'POST':
    #     form = RatingForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     else:
    #         print("Form errors:", form.errors)
    #         return render(request, 'core/index.html', {'form': form})
    
    # if request.method == 'POST':
    #     form = RatingForm(request.POST or None)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #     else:
    #         return render(request,'core/index.html',{'form':form})
    
    if request.method == 'POST':
        form = RestaurentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Form errors:", form.errors)
            return render(request, 'core/index.html', {'form': form})
    
    return render(request, 'core/index.html', {'form': RestaurentForm()})
    
# from django.contrib.auth.models import User
# from django.utils import timezone
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from decimal import Decimal
# from random import randint, choice, uniform
# from datetime import datetime, timedelta, date

# from .models import Restaurent, Rating, Sale

# @api_view(['POST'])
# def populate_sample_data(request):
#     # Sample Users
#     users = []
#     for i in range(5):
#         user, _ = User.objects.get_or_create(
#             username=f'user{i}',
#             defaults={'email': f'user{i}@example.com', 'password': 'testpass123'}
#         )
#         users.append(user)

#     # Sample Restaurants
#     types = ['IN', 'CH', 'IT', 'GR', 'MX', 'FF', 'OT']
#     names = ['Annapurna', 'Dragon Wok', 'La Pasta', 'Greek Gyro', 'Taco Fiesta', 'Burger Hub', 'Global Eats']
#     restaurants = []

#     for i, name in enumerate(names):
#         rest, _ = Restaurent.objects.get_or_create(
#             name=name,
#             defaults={
#                 'website': f'https://www.{name.lower().replace(" ", "")}.com',
#                 'date_opened': date(2010+i, 5, 15),
#                 'latitute': round(uniform(-90, 90), 6),
#                 'longitute': round(uniform(-180, 180), 6),
#                 'restaurent_type': types[i % len(types)],
#             }
#         )
#         restaurants.append(rest)

#     # Sample Ratings
#     for user in users:
#         for rest in restaurants:
#             if randint(0, 1):  # 50% chance of rating
#                 Rating.objects.get_or_create(
#                     user=user,
#                     restaurent=rest,
#                     defaults={'rating': randint(1, 5)}
#                 )

#     # Sample Sales
#     for rest in restaurants:
#         for _ in range(5):  # 5 sales per restaurant
#             Sale.objects.create(
#                 restaurent=rest,
#                 income=Decimal(randint(1000, 10000)) + Decimal(f".{randint(0,99):02d}"),
#                 datetime=timezone.now() - timedelta(days=randint(0, 365))
#             )

#     return Response({"message": "Sample data created successfully!"})
