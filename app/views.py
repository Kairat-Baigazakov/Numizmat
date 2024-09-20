from django.shortcuts import render, get_object_or_404, redirect
from .models import CoinObj
from .forms import CoinObjForm
from django.contrib import auth


# Тут мы создаем сами Views в виде функции/методов которые принимают request
def index(request):
    coins = CoinObj.objects.all()
    return render(request, 'app/index.html', {'coins': coins})


def coin_detail(request, pk):
    coin = get_object_or_404(CoinObj, pk=pk)
    return render(request, 'app/coin_detail.html', {'coin': coin})


def coin_add(request):
    if request.method == "POST":
        form = CoinObjForm(request.POST)
        if form.is_valid():
            coin = form.save(commit=False)
            coin.save()
            return redirect('coin_detail', pk=coin.pk)
    else:
        form = CoinObjForm()
    return render(request, 'app/coin_edit.html', {'form': form})


def coin_edit(request, pk):
    coin = get_object_or_404(CoinObj, pk=pk)
    if request.method == "POST":
        form = CoinObjForm(request.POST, instance=coin)
        if form.is_valid():
            coin = form.save(commit=False)
            coin.save()
            return redirect('coin_detail', pk=coin.pk)
    else:
        form = CoinObjForm(instance=coin)
    return render(request, 'app/coin_edit.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return redirect('login_user')
    else:
        return render(request, 'app/login.html')


def info(request):
    return render(request, 'app/info.html')
