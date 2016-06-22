from django.shortcuts import render
from django.http import HttpResponse


def groups_list(request):
    return render(request, 'students/groups_list.html', {})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Groups %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)