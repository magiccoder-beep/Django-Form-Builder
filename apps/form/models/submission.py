from django.db import models
from .form import Form
from .field import Field

class Submission(models.Model):
    form = models.ForeignKey(Form, related_name='submissions', on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)

class FieldSubmission(models.Model):
    submission = models.ForeignKey(Submission, related_name='field_submissions', on_delete=models.CASCADE)
    field = models.ForeignKey(Field, related_name='submissions', on_delete=models.CASCADE)
    value = models.TextField()

    class Meta:
        unique_together = ('submission', 'field')