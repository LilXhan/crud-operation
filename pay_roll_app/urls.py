from django.urls import path

from . import views

urlpatterns = [
    path('employees-list', views.employees_list, name='employees-list'),
    path('employee-details/<int:id>', views.employee_details, name='employee-details'),
    path('employee-delete/<int:id>', views.employee_delete, name='employee-delete'),
    path('employee-update/<int:id>', views.employee_update, name='employee-update'),
    path('employee-insert', views.employee_insert, name='employee-insert')
]