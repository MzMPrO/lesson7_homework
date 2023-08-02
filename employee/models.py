from django.db import models

from department.models import Department
from profession.models import Profession


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    profession_id = models.ForeignKey(Profession, on_delete=models.CASCADE)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
