from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import MyUser

# Create your views here.
def userinfo(res, user_id):
    user = get_object_or_404(MyUser, pk=user_id)
    return render(res, 'users/info.html', {'user': user})

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
