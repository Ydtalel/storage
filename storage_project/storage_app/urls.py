from django.urls import path

from storage_app.views import get_storage

urlpatterns = [
    path('storage/', get_storage, name='storage'),
]
