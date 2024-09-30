from django import forms

from .models import Employee

# Creating a Form Based Model

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

        widgets = {
            'birth_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'hire_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }