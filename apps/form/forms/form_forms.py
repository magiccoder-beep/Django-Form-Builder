from django import forms
from ..models import Form, Step, Element, Field, Submission, FieldSubmission

class FormCreateForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['name', 'description']

class StepCreateForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = ['form', 'title', 'order']

class ElementCreateForm(forms.ModelForm):
    class Meta:
        model = Element
        fields = ['step', 'type', 'order', 'style']

class FieldCreateForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = ['element', 'field_type', 'label', 'options']

class SubmissionCreateForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['form']

class FieldSubmissionCreateForm(forms.ModelForm):
    class Meta:
        model = FieldSubmission
        fields = ['submission', 'field', 'value']

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