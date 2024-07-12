from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from ..models import Form, Step, Field, Element
from apps.form.dynamic_form import DynamicForm

def form_list(request):
    forms = Form.objects.all()
    return render(request, 'form_list.html', {'forms': forms})

def form_detail(request, form_id):
    form = get_object_or_404(Form, id=form_id)
    steps = form.steps.all()
    return render(request, 'form_detail.html', {'form': form, 'steps': steps})

def step_form(request, form_id, step_id):
    form = get_object_or_404(Form, id=form_id)
    step = get_object_or_404(Step, id=step_id, form=form)
    elements = step.elements.filter(type='field').select_related('field')
    fields = [element.field for element in elements]

    if request.method == 'POST':
        form_instance = DynamicForm(request.POST, fields=fields)
        if form_instance.is_valid():
            # Process the form data here
            next_step = Step.objects.filter(form=form, order=step.order + 1).first()
            if next_step:
                return redirect('step_form', form_id=form.id, step_id=next_step.id)
            else:
                return redirect('form_detail', form_id=form.id)
    else:
        form_instance = DynamicForm(fields=fields)

    return render(request, 'step_form.html', {'form': form_instance, 'step': step})