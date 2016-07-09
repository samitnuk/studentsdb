from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from django.views.generic import DeleteView

from ..models.groups import Group
from ..utils import paginate


def groups_list(request):
    groups = Group.objects.all()

    # try to order groups list
    order_by = request.GET.get('order_by', '')
    if order_by in ('id', 'title', 'leader'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()

    # order by title if page loads first time
    else:
        groups = groups.order_by('title')

    groups = paginate(groups, 3, request, {}, var_name='groups')

    return render(request, 'students/groups_list.html', groups)


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, pk):
    return HttpResponse('<h1>Edit Groups %s</h1>' % pk)


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'students/groups_confirm_delete.html'

    def get_success_url(self):
        return "%s?status_message=Групу успішно видалено!" \
            % reverse('home')
