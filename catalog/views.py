from django.shortcuts import render
from catalog.models import Employee


def show_employees(request):
    return render(request, "index.html", {'employees': Employee.objects.all()})