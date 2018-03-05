from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'django-twitter-api', 'url': 'http://pypi.python.org/pypi/django-twitter-api/0.2.10'},
	{'name':'django-paypal', 'url': 'http://pypi.python.org/pypi/django-paypal/0.4.1'},
	{'name':'django-twitter', 'url': 'http://pypi.python.org/pypi/django-twitter/0.1.0'},
    ]
    context = {
        'title': 'sgmagar-crowdbotics-64',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
