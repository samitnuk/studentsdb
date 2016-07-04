from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models.exams import Exam


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

    # paginate exams
    paginator = Paginator(exams, 3)
    page = request.GET.get('page')
    try:
        exams = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page
        exams = paginator.page(1)
    except EmptyPage:
        # if page is oout of range (e.g. 9999), deliver
        # last page of results
        exams = paginator.page(paginator.num_pages)

    return render(request, 'students/exams_list.html',
                  {'exams': exams})


def exams_add(request):
    return HttpResponse('<h1>Exams Add Form</h1>')


def exams_edit(request, eid):
    return HttpResponse('<h1>Edit Exam %s</h1>' % eid)


def exams_delete(request, eid):
    return HttpResponse('<h1>Delete Exam %s</h1>' % eid)
