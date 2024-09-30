from django.db import models


class Department(models.Model):
    department_name = models.CharField(max_length=30)
    location_name = models.CharField(max_length=30)

    def __str__(self):
        return self.department_name
    

class Country(models.Model):
    country_name = models.CharField(max_length=30)

    def __str__(self):
        return self.country_name


class Employee(models.Model):

    # COUNTRIES = [
    #     ('IND', 'INDIA'),
    #     ('USA', 'United States Of America'),
    #     ('UK', 'United Kingdom'),
    #     ('AUS', 'AUSTRALIA'),
    #     ('AU', 'AUSTRIA'),
    #     ('SP', 'SPAIN')
    # ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    title_name = models.CharField(max_length=30)
    has_passport = models.BooleanField()
    salary = models.IntegerField()
    birth_date = models.DateField()
    hire_date = models.DateField()
    notes = models.CharField(max_length=200)
    # country = models.CharField(max_length=35, choices=COUNTRIES, default=None)
    email = models.EmailField(default="", max_length=50)
    phone_number = models.CharField(default="", max_length=20)
    employee_department = models.ForeignKey("Department", default=0, on_delete=models.PROTECT, related_name="Deparment")
    employee_country = models.ForeignKey("Country", default=0, on_delete=models.PROTECT, related_name="Country")