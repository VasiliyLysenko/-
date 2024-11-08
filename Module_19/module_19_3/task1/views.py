from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import UserRegister
from .models import *
from django.http import HttpResponse


class Platform(TemplateView):
    template_name = 'platform.html'


class Cart(TemplateView):
    template_name = 'cart.html'


def menu(request):
    mydict = Game.objects.all()
    context = {
        'mydict': mydict,
    }
    return render(request, 'games.html', context)

def sign_up_by_django(request):
    users = Buyer.objects.all()
    usernames = [i.name for i in users]
    i = 0
    info = {'error': []}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if username not in usernames and password == repeat_password and int(age) >= 18:
                Buyer.objects.create(name=username, balance=0, age=age)
                context = {'username': username}
                return render(request, 'registration_complete.html', context)
            elif username in usernames:
                i += 1
                info[f'error {i}'] = HttpResponse('Пользователь уже существует', status=400, reason='repeated login')
                print(info[f'error {i}'])
                return HttpResponse('Пользователь уже существует', status=400, reason='repeated login')
            elif password != repeat_password:
                i += 1
                info[f'error {i}'] = HttpResponse('Пользователь уже существует', status=400, reason='repeated login')
                print(info[f'error {i}'])
                return HttpResponse('Пароли не совпадают', status=400, reason='non-identical passwords')
            elif int(age) < 18:
                i += 1
                info[f'error {i}'] = HttpResponse(
                    f'Вы должны быть старше 18', status=400, reason='insufficient age')

                return HttpResponse(
                    f'Вы должны быть старше 18', status=400, reason='insufficient age')
    else:

        form = UserRegister()
        context = {'info': info, 'form': form}
        return render(request, 'registration_page.html', context)