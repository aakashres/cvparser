from django.db import models

# Create your models here.

FILE_CHOICES = (
    (1, 'PDF'),
    (2, 'DOC')
)


class CV(models.Model):
    file = models.FileField()
    filetype = models.PositiveIntegerField(default=1, choices=FILE_CHOICES)