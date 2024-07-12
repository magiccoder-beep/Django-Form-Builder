from django.db import models
from .form import Form

MAX_STEP_TITLE_LENGTH = 255

class Step(models.Model):
    form = models.ForeignKey(Form, related_name="steps", on_delete=models.CASCADE)
    title = models.CharField(max_length = MAX_STEP_TITLE_LENGTH)
    order = models.PositiveIntegerField()
    
    class Meta:
        ordering = ['order']