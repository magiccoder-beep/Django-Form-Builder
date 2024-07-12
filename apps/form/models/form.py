from uuid import uuid4
from django.db import models

MAX_FORM_NAME_LENGTH=128

class Form(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=MAX_FORM_NAME_LENGTH, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)