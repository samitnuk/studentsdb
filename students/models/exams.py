from django.db import models


class Exam(models.Model):
    """Exam Model"""

    class Meta(object):
        verbose_name = 'Іспит'
        verbose_name_plural = 'Іспити'

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='Назва предмету')

    datetime = models.DateTimeField(
        blank=False,
        verbose_name='Дата і час проведення')

    teacher = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='ПІБ викладача')

    exam_group = models.ForeignKey(
        'Group',
        verbose_name='Група',
        blank=False,
        null=True,
        on_delete=models.PROTECT)

    def __str__(self):
        return '%s (приймає %s' % (self.title, self.teacher)
