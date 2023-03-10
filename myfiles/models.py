from django.db import models

# Create your models here.
class Type(models.Model):
    nomi = models.CharField(max_length=30)
    def __str__(self):
        return self.nomi

class Maxsulot(models.Model):
    nomi = models.CharField(max_length=30)
    rasmi = models.CharField(max_length=200)
    narxi = models.IntegerField()
    text = models.TextField(blank=True,null=True)
    tur = models.ForeignKey(Type,on_delete=models.CASCADE)


class Menu(models.Model):
    nomi = models.CharField(max_length=30)
    def __str__(self):
        return self.nomi


class Azolar(models.Model):
    ism = models.CharField(max_length=30)
    fam = models.CharField(max_length=30,null=True,blank=True)
    username = models.CharField(max_length=30,null=True,blank=True)
    tg_id = models.IntegerField(unique=True)




