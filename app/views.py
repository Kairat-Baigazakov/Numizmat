from django.shortcuts import render, get_object_or_404, redirect
from .models import CoinObj
from .forms import CoinForm


# Тут мы создаем сами Views в виде функции/методов которые принимают request
def index(request):
    coins = CoinObj.objects.all()
    return render(request, 'app/index.html', {'coins': coins})


def coin_detail(request, pk):
    coin = get_object_or_404(CoinObj, pk=pk)
    return render(request, 'app/coin_detail.html', {'coin': coin})


def coin_add(request):
    if request.method == "POST":
        form = CoinForm(request.POST)
        if form.is_valid():
            coin = form.save(commit=False)
            coin.nominal = 100
            coin.weight = 30
            coin.diameter = 10
            coin.save()
            return redirect('coin_detail', pk=coin.pk)
    else:
        form = CoinForm()
    return render(request, 'app/coin_edit.html', {'form': form})


def coin_edit(request, pk):
    coin = get_object_or_404(CoinObj, pk=pk)
    if request.method == "POST":
        form = CoinForm(request.POST, instance=coin)
        if form.is_valid():
            coin = form.save(commit=False)
            coin.save()
            return redirect('coin_detail', pk=coin.pk)
    else:
        form = CoinForm(instance=coin)
    return render(request, 'app/coin_edit.html', {'form': form})


def info(request):
    return render(request, 'app/info.html')
