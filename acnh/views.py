from django.shortcuts import render
import requests

# Create your views here.
def index(req):
    fish_data = {}
    name_set = {}
    if 'fish_name' in req.GET:
        fish_name = req.GET['fish_name']
        url = 'http://acnhapi.com/v1/fish/%s' % fish_name
        response = requests.get(url)
        fish_data = response.json()
        name_set = fish_data['name']
    return render(req, 'acnh/index.html', {
        'fish_name': name_set['name-CNzh'],
        'fish_data': fish_data
        })
