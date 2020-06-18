from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.index, name='home'),
    # path('work/', views.work, name='work')
]
