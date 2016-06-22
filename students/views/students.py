from django.shortcuts import render
from django.http import HttpResponse


def students_list(request):
    students = (
        {'id': 1,
         'first_name': 'Віталій',
         'last_name': 'Подоба',
         'ticket': 235,
         'image': 'img/image1.jpg'},
        {'id': 2,
         'first_name': 'Андрій',
         'last_name': 'Корост',
         'ticket': 2435,
         'image': 'img/image2.jpg'},
         {'id': 3,
         'first_name': 'Іван',
         'last_name': 'Драган',
         'ticket': 7235,
         'image': 'img/image3.jpg'},
    )
    return render(request, 'students/students_list.html',
        {'students': students})

def students_add(request):
    return HttpResponse('<h1>Students Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)