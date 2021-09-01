import datetime
from django.utils import timezone
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    date_published = models.DateField(default=timezone.now)
    description = models.TextField()

    def __str__(self):
        return self.title

