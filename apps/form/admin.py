from django.contrib import admin
from .models import Form, Step, Element, Submission, FieldSubmission, Button, Text

admin.site.register(Form)
admin.site.register(Step)
admin.site.register(Element)
admin.site.register(Submission)
admin.site.register(FieldSubmission)
admin.site.register(Button)
admin.site.register(Text)