from django.db import models
from django.utils import timezone
import datetime as dt
# Create your models here.


class Tmbcamcount (models.Model):
    date = models.DateField(default=dt.datetime(1984, 5, 17))
    timeCC = models.TimeField(default=dt.time(12, 0, 0))
    dealer = models.IntegerField(default=0)
    pickup = models.IntegerField(default=0)
    rnd = models.IntegerField(default=0)
    smallGal = models.IntegerField(default=0)
    squareGal = models.IntegerField(default=0)
    dealCust = models.IntegerField(default=0)
    dayparts = models.TextField(blank=True)
    suspectText = models.TextField(blank=True)


class Labcamcount(models.Model):
    date = models.DateField(default=dt.datetime(1984, 5, 17))
    timeCC = models.TimeField(default=dt.time(12, 0, 0))
    dealer = models.IntegerField(default=0)
    pickup = models.IntegerField(default=0)
    rnd = models.IntegerField(default=0)
    smallGal = models.IntegerField(default=0)
    squareGal = models.IntegerField(default=0)
    dealCust = models.IntegerField(default=0)
    dayparts = models.TextField(blank=True)
    suspectText = models.TextField(blank=True)


class Kalcamcount(models.Model):
    date = models.DateField(default=dt.datetime(1984, 5, 17))
    timeCC = models.TimeField(default=dt.time(12, 0, 0))
    dealer = models.IntegerField(default=0)
    pickup = models.IntegerField(default=0)
    rnd = models.IntegerField(default=0)
    smallGal = models.IntegerField(default=0)
    squareGal = models.IntegerField(default=0)
    dealCust = models.IntegerField(default=0)
    dayparts = models.TextField(blank=True)
    suspectText = models.TextField(blank=True)


class Goldswancamcount(models.Model):
    date = models.DateField(default=dt.datetime(1984, 5, 17))
    timeCC = models.TimeField(default=dt.time(12, 0, 0))
    dealer = models.IntegerField(default=0)
    pickup = models.IntegerField(default=0)
    rnd = models.IntegerField(default=0)
    smallGal = models.IntegerField(default=0)
    squareGal = models.IntegerField(default=0)
    dealCust = models.IntegerField(default=0)
    dayparts = models.TextField(blank=True)
    suspectText = models.TextField(blank=True)
