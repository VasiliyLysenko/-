from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request, 'platform.html')


class Cart(TemplateView):
    template_name =  'cart.html'


def Shop(request):
    mydict = {'games': ["Atomic Heart", "Cyberpunk 2077", "Pay Day 2"]}
    context = {
        'mydict': mydict,
    }
    return render(request, 'games.html', context)