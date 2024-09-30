from django.shortcuts import render, redirect

from .models import Employee
from .forms import EmployeeForm

def employees_list(request):
    # employees = Employee.objects.all()

    employees = Employee.objects.select_related('employee_department', 'employee_country')
    dict = {
        'employees': employees
    }
    template_file = 'pay_roll_app/employees_list.html'

    return render(request, template_file, dict)


def employee_details(request, id):
    # employee = Employee.objects.get(id=id)

    employee = Employee.objects.select_related('employee_department', 'employee_country').get(id=id)

    dict = {
        'employee': employee
    }
    template_file = 'pay_roll_app/employee_details.html'

    return render(request, template_file, dict)


def employee_delete(request, id):
    # employee = Employee.objects.get(id=id)

    employee = Employee.objects.select_related('employee_department', 'employee_country').get(id=id)
    dict = {
        'employee': employee
    }
    template_file = 'pay_roll_app/employee_delete.html'

    if request.method == 'POST':
        employee.delete()
        return redirect('employees-list')


    return render(request, template_file, dict)


def employee_update(request, id):
    # employee = Employee.objects.get(id=id)

    employee = Employee.objects.select_related('employee_department', 'employee_country').get(id=id)

    form = EmployeeForm(instance=employee)
    dict = {
        'form': form
    }
        
    template_file = 'pay_roll_app/employee_update.html'
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('employees-list')

    return render(request, template_file, dict)


def employee_insert(request):
    form = EmployeeForm()
    template_file = 'pay_roll_app/employee_insert.html'
    dict = {
        'form': form
    }

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('employees-list')

    return render(request, template_file, dict)
