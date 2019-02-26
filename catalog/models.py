from django.db import models
from django.urls import reverse


class FIO(models.Model):
    fio = models.CharField(max_length = 150, name = 'ФИО')

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.fio

class Employee(models.Model):
    fio = models.ForeignKey('FIO', on_delete=models.SET_NULL, null = True, name='ФИО')
    date = models.DateField(null=True, blank=True, name='Дата приема на работу')
    salary = models.IntegerField(name = 'Зарплата')
    position = models.ForeignKey('Position', on_delete=models.SET_NULL, null=True, name = 'Должность')
    



class Position(models.Model):
 
    department = models.CharField(max_length = 100, name = 'Отдел')
    position = models.CharField(max_length = 45, name = 'Должность')
    boss = models.ForeignKey('FIO', on_delete=models.SET_NULL, null =True, name = 'Начальник')





