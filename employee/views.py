from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from datetime import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q


from .models import Employee
from .forms import EmployeeForm, LoginFormm

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login



def login_view(request):
    form = LoginFormm()

    if request.method == 'POST':
        form = LoginFormm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('index')  # Redirect to the 'index' URL
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginFormm()
    
    return render(request, 'user/login.html', {'form':form})

# Rest of the code...

@login_required
def index(request):
    

    employees = Employee.objects.all()

    if 'q' in request.GET:
        q = request.GET['q']
        employees = Employee.objects.filter(name__icontains=q) 
    else:
        employees = Employee.objects.all()

    # Specify the number of employees per page
    items_per_page = 5

    # Create a Paginator object
    paginator = Paginator(employees, items_per_page)

    # Get the current page number from the query parameters
    page_number = request.GET.get('page')

    # Get the Page object for the current page
    page = paginator.get_page(page_number)

    return render(request, 'employee/index.html', {
        'employees': page,
    })

@login_required
def view_employee(request, id):
    employee = Employee.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))
@login_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            new_employee_id = form.cleaned_data['employee_id'] 
            new_gender = form.cleaned_data['gender'] 
            new_dob = datetime.strptime(form.cleaned_data['dob'].strftime('%d/%m/%Y'), '%d/%m/%Y').date()
            new_designation = form.cleaned_data['designation']
            new_department = form.cleaned_data['department']
            new_appointment_date = datetime.strptime(form.cleaned_data['appointment_date'].strftime('%d/%m/%Y'), '%d/%m/%Y').date()

            new_employee = Employee(
                name=new_name,
                employee_id=new_employee_id,
                gender=new_gender,
                dob=new_dob,
                designation=new_designation,
                department=new_department,
                appointment_date=new_appointment_date
            )
            new_employee.save()
            return render(request, 'employee/add_employee.html', {
                'form': EmployeeForm(),
                'success': True
            })
    else:
        form = EmployeeForm()
    return render(request, 'employee/add_employee.html', {
        'form': EmployeeForm()
    })
@login_required
def edit(request, id):
    if request.method == 'POST':
        employee = Employee.objects.get(pk=id)
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return render(request, 'employee/edit.html', {
                'form': form,
                'success': True
            })
    else:
        employee = Employee.objects.get(pk=id)
        form = EmployeeForm(instance=employee)
    return render(request, 'employee/edit.html', {
        'form': form
    })
@login_required
def delete(request, id):
    if request.method =='POST':
        employee = Employee.objects.get(pk=id)
        employee.delete()
    return HttpResponseRedirect(reverse('index'))