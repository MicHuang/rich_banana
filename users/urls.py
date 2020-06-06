from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    # ex: /users/search/
    path('search/', views.search, name='search'),
    # ex: /users/5
    path('<int:pk>', views.UserView.as_view(), name='info')
]
