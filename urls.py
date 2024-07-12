from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', include('apps.form.urls')),  # Include the URLs from the form app
]
