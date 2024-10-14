from django.urls import path
from .views import list_carros, form_1

urlpatterns = [
    path('', list_carros),
    path('new/', form_1,name='form_1')
]
