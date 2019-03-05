from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Employee(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    position = models.CharField(max_length=50, verbose_name = 'Должность')
    date = models.DateField(verbose_name= 'Дата приема на работу')
    salary = models.IntegerField(verbose_name='Зарплата')
    
    def __str__(self):
	    return self.name

    class MPTTMeta:
        order_insertion_by = ['name']





