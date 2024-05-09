from django.db import models
import uuid

class Note(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=250)
    body = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.title
