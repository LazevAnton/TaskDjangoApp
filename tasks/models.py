import uuid
from django.db import models


class TasksModel(models.Model):
    STATUS_CHOICE = [
        ('inprogress', 'INPROGRESS'),
        ('completed', 'COMPLETED')
    ]
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task_status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='inprogress')
    reporter = models.ForeignKey("users.UserModel", on_delete=models.PROTECT, related_name='reporter_user')
    assignee = models.ForeignKey("users.UserModel", on_delete=models.PROTECT, related_name='assignee_user')

    def __str__(self):
        return f'{self.reporter} - {self.title}'
