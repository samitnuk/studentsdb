from django.contrib import admin
from django.core.urlresolvers import reverse
from django.forms import ModelForm, ValidationError

from .models.students import Student
from .models.groups import Group
from .models.exams import Exam


class StudentAdminForm(ModelForm):

    def clean_student_group(self):
        """Check if student is leader in any group.
        If yes, then ensure it's the same as selected group."""
        # get group where current student is leader
        groups = Group.objects.filter(leader=self.instance)
        if len(groups) > 0 and \
            self.cleaned_data['student_group'] != groups[0]:
            raise ValidationError("Студент є старостою іншої групи.",
                code='invalid')

        return self.cleaned_data['student_group']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'ticket', 'student_group']
    list_display_links = ['last_name', 'first_name']
    list_editable = ['student_group']
    ordering = ['last_name']
    list_filter = ['student_group']
    list_per_page = 10
    search_fields = ['last_name', 'first_name', 'middle_name', 'ticket',
                     'notes']
    form = StudentAdminForm

    def view_on_site(self, obj):
        return reverse('students_edit', kwargs={'pk': obj.id})

class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'leader']
    list_display_links = ['title']
    list_editable = ['leader']
    ordering = ['title']
    # list_filter = ['title']
    list_per_page = 10
    search_fields = ['tile', 'leader']

    def view_on_site(self, obj):
        return reverse('groups_edit', kwargs={'pk': obj.id})

admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Exam)