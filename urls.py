from django.urls import path

from . import views
from .views import ConsCreate

urlpatterns = [
    path('', ConsCreate.as_view(), name='create_url'),
    path('create/', views.index, name='index')
]
