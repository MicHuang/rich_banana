from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import MyUser

# Create your views here.
class UserView(generic.DetailView):
    model = MyUser
    template_name = 'users/info.html'
    context_object_name = 'user'

# Create user API view
class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer

def search(res):
    if res.method == 'POST':
        try:
            user = get_object_or_404(MyUser, phone=res.POST['phone'])
        except Exception as e:
            # Redisplay the search form with error_message
            return render(res, 'users/search.html', {
                'error_message': "User not exist."
            })
        else: return HttpResponseRedirect(reverse('users:info', args=(user.id,)))
    else: return render(res, 'users/search.html', {})
