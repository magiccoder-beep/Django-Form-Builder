from django.db import models
from jsonfield import JSONField
from .element import Element

class Field(models.Model):
    FIELD_TYPES = [
        ('text', 'Text Field'),
        ('dropdown', 'Dropdown'),
        ('checkbox', 'Checkbox Group')
    ]

    element = models.OneToOneField(Element, related_name='field', on_delete=models.CASCADE)
    field_type = models.CharField(max_length=10, choices=FIELD_TYPES)
    label = models.CharField(max_length=255)
    options = JSONField(default=list, blank=True)
