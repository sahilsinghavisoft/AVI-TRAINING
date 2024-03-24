from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)  # Add due_date field
    completion_time = models.DateTimeField(null=True, blank=True)  # Correct to DateTimeField

    def __str__(self):
        return self.title
