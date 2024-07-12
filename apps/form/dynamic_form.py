from django import forms
from .models import Field

class DynamicForm(forms.Form):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields')
        super(DynamicForm, self).__init__(*args, **kwargs)
        for field in fields:
            if field.field_type == 'text':
                self.fields[field.label] = forms.CharField(label=field.label)
            elif field.field_type == 'dropdown':
                self.fields[field.label] = forms.ChoiceField(choices=[(opt, opt) for opt in field.options], label=field.label)
            elif field.field_type == 'checkbox':
                self.fields[field.label] = forms.MultipleChoiceField(choices=[(opt, opt) for opt in field.options], label=field.label, widget=forms.CheckboxSelectMultiple)
