from django.shortcuts import render, redirect
from .forms import registerForm

# Create your views here.
def register(res):
    if res.method == 'POST':
        form = registerForm(res.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = registerForm()
    return render(res, 'register/register.html', {'form': form})
