from django.db import models


class Type(models.Model):
    title = models.CharField(max_length=30)
    proba = models.PositiveIntegerField()
    technology = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Theme(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Coin(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()

    def __str__(self):
        return self.title


class CoinObj(models.Model):
    nominal = models.PositiveSmallIntegerField()
    weight = models.FloatField()
    diameter = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    title = models.ForeignKey(Coin, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title.title} - {self.type.title}'
