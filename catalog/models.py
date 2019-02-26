from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length = 45, name = 'Имя')
    last_name = models.CharField(max_length = 45, name = 'Фамилия')
    middle_name = models.CharField(max_length = 45, name = 'Отчество')
    date = models.DateField(null=True, blank=True)
    position = models.ForeignKey('Position', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        
        return self.last_name


class Position(models.Model):
    #first_name = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True) 
    #last_name = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True)
    #middle_name = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True)
    department = models.CharField(max_length = 100)
    position = models.CharField(max_length = 45, name = 'Должность')
    boss = models.ForeignKey('Employee', on_delete=models.SET_NULL, null =True)

    def __str__(self):
        
        return self.position



