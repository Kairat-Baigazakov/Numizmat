from django.contrib import admin
from .models import Coin, Type, Theme, CoinObj

admin.site.register(Coin)
admin.site.register(Type)
admin.site.register(Theme)
admin.site.register(CoinObj)
