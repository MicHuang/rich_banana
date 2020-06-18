from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'portfolio/index.html', {'about': 'active'})

# def work(req):
#     return render(req, 'portfolio/work.html', {'work': 'active'})
