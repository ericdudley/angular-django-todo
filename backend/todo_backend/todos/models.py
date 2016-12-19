from django.db import models
from django.utils import timezone

class ToDo(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    time_finished = models.DateTimeField(null=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    text = models.TextField()
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        if self.finished:
            self.time_finished = timezone.now()
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-time_created']
