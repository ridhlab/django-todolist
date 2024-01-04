from django.db import models
import uuid


# Create your models here.
class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    is_completed = models.BooleanField(default=False)

    class Meta:
        db_table = "todo"
