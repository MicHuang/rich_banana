from django.urls import path
from . import views

app_name = 'acnh'
urlpatterns = [
    # ex: /acnh/
    path('', views.index, name='index')
]
