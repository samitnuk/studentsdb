from django.shortcuts import render
from django.http import HttpResponse

from ..models.exams import Exam
from ..utils import paginate


def exams_list(request):
    exams = Exam.objects.all()

    # try to order exams list
    order_by = request.GET.get('order_by', '')
    if order_by in ('id', 'title', 'teacher', 'exam_group'):
        exams = exams.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            exams = exams.reverse()

    # order by title if page loads firs time
    else:
        exams = exams.order_by('title')

    exams = paginate(exams, 3, request, {}, var_name='exams')

    return render(request, 'students/exams_list.html',
                  exams)


def exams_add(request):
    return HttpResponse('<h1>Exams Add Form</h1>')


def exams_edit(request, eid):
    return HttpResponse('<h1>Edit Exam %s</h1>' % eid)


def exams_delete(request, eid):
    return HttpResponse('<h1>Delete Exam %s</h1>' % eid)
