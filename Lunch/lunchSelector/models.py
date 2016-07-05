from django.db import models


class Menu(models.Model):
    menu_text = models.CharField(max_length=30)
    count = models.IntegerField(default=0)
    count_permanent = models.IntegerField(default=0)


class Order(models.Model):
    o_menu_text = models.CharField(max_length=30)
    date = models.DateTimeField('date_published')


# Create your models here.
