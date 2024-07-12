from django.urls import path
from .views import form_views

urlpatterns = [
    path('', form_views.form_list, name='form_list'),
    path('<uuid:form_id>/', form_views.form_detail, name='form_detail'),
    path('<uuid:form_id>/step/<int:step_id>/', form_views.step_form, name='step_form'),
]
