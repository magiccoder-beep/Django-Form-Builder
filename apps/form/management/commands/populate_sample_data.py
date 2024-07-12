from django.core.management.base import BaseCommand
from apps.form.models import Form, Step, Element, Button, Text, Field
import uuid

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        sample_data = [
            {
                "form": {
                    "name": "Registration Form"
                },
                "steps": [
                    {
                        "title": "Step 1: Personal Information",
                        "order": 1,
                        "elements": [
                            {
                                "type": "field",
                                "order": 1,
                                "field_type": "text",
                                "label": "First Name",
                                "options": []
                            },
                            {
                                "type": "field",
                                "order": 2,
                                "field_type": "text",
                                "label": "Last Name",
                                "options": []
                            }
                        ]
                    },
                    {
                        "title": "Step 2: Account Information",
                        "order": 2,
                        "elements": [
                            {
                                "type": "field",
                                "order": 1,
                                "field_type": "text",
                                "label": "Email",
                                "options": []
                            },
                            {
                                "type": "field",
                                "order": 2,
                                "field_type": "password",
                                "label": "Password",
                                "options": []
                            }
                        ]
                    }
                ]
            },
            {
                "form": {
                    "name": "Feedback Form"
                },
                "steps": [
                    {
                        "title": "Step 1: General Information",
                        "order": 1,
                        "elements": [
                            {
                                "type": "field",
                                "order": 1,
                                "field_type": "text",
                                "label": "Name",
                                "options": []
                            },
                            {
                                "type": "field",
                                "order": 2,
                                "field_type": "email",
                                "label": "Email",
                                "options": []
                            }
                        ]
                    },
                    {
                        "title": "Step 2: Feedback",
                        "order": 2,
                        "elements": [
                            {
                                "type": "field",
                                "order": 1,
                                "field_type": "textarea",
                                "label": "Comments",
                                "options": []
                            }
                        ]
                    }
                ]
            },
            {
                "form": {
                    "name": "Survey Form"
                },
                "steps": [
                    {
                        "title": "Step 1: Introduction",
                        "order": 1,
                        "elements": [
                            {
                                "type": "text",
                                "order": 1,
                                "content": "Please provide your feedback."
                            }
                        ]
                    },
                    {
                        "title": "Step 2: Questions",
                        "order": 2,
                        "elements": [
                            {
                                "type": "field",
                                "order": 1,
                                "field_type": "dropdown",
                                "label": "How satisfied are you with our service?",
                                "options": ["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"]
                            },
                            {
                                "type": "field",
                                "order": 2,
                                "field_type": "text",
                                "label": "Comments",
                                "options": []
                            }
                        ]
                    }
                ]
            },
            {
                "form": {
                    "name": "Job Application Form"
                },
                "steps": [
                    {
                        "title": "Step 1: Personal Details",
                        "order": 1,
                        "elements": [
                            {
                                "type": "field",
                                "order": 1,
                                "field_type": "text",
                                "label": "Full Name",
                                "options": []
                            },
                            {
                                "type": "field",
                                "order": 2,
                                "field_type": "email",
                                "label": "Email Address",
                                "options": []
                            }
                        ]
                    },
                    {
                        "title": "Step 2: Experience",
                        "order": 2,
                        "elements": [
                            {
                                "type": "field",
                                "order": 1,
                                "field_type": "text",
                                "label": "Work Experience",
                                "options": []
                            }
                        ]
                    }
                ]
            },
            {
                "form": {
                    "name": "Event Registration Form"
                },
                "steps": [
                    {
                        "title": "Step 1: Contact Information",
                        "order": 1,
                        "elements": [
                            {
                                "type": "field",
                                "order": 1,
                                "field_type": "text",
                                "label": "Name",
                                "options": []
                            },
                            {
                                "type": "field",
                                "order": 2,
                                "field_type": "email",
                                "label": "Email",
                                "options": []
                            }
                        ]
                    },
                    {
                        "title": "Step 2: Event Details",
                        "order": 2,
                        "elements": [
                            {
                                "type": "field",
                                "order": 1,
                                "field_type": "dropdown",
                                "label": "Select Event",
                                "options": ["Event A", "Event B", "Event C"]
                            }
                        ]
                    }
                ]
            }
        ]

        for form_data in sample_data:
            form = Form.objects.create(name=form_data["form"]["name"])
            for step_data in form_data["steps"]:
                step = Step.objects.create(form=form, title=step_data["title"], order=step_data["order"])
                for element_data in step_data["elements"]:
                    element = Element.objects.create(step=step, type=element_data["type"], order=element_data["order"])
                    if element_data["type"] == "text":
                        Text.objects.create(element=element, content=element_data["content"])
                    elif element_data["type"] == "button":
                        Button.objects.create(element=element, label=element_data["label"], action=element_data["action"])
                    elif element_data["type"] == "field":
                        Field.objects.create(element=element, field_type=element_data["field_type"], label=element_data["label"], options=element_data["options"])

        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))
