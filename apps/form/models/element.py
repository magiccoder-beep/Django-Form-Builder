from django.db import models
from jsonfield import JSONField
from .step import Step
import uuid

class Element(models.Model):
    STEP_ELEMENT_TYPES = [
        ('text', 'Text'),
        ('button', 'Button'),
        ('field', 'Field')
    ]

    step = models.ForeignKey(Step, related_name='elements', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=STEP_ELEMENT_TYPES)
    order = models.PositiveIntegerField()
    style = JSONField(default=dict, blank=True)

    class Meta:
        ordering = ['order']

class Button(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    element = models.OneToOneField(Element, related_name='button', on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    action = models.CharField(max_length=255)

class Text(models.Model):
    element = models.OneToOneField(Element, related_name='text', on_delete=models.CASCADE)
    content = models.TextField()
