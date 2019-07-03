from django.db import models

# Create your models here.
class employee(models.Model):
    employee_no=models.IntegerField()
    employee_name=models.CharField(max_length=50)
    employee_salary=models.IntegerField()
    employee_city=models.CharField(max_length=50)
    def __str__(self):
        return self.employee_name