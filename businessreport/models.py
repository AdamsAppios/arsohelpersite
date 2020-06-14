from django.db import models
import datetime
# Create your models here.


class Tmbreport (models.Model):
    dateReport = models.DateField()
    dealer = models.IntegerField(default=0)
    pickup = models.IntegerField(default=0)
    rndgal = models.IntegerField(default=0)
    rndEnd = models.IntegerField(default=0)
    badgermeter = models.IntegerField(default=0)
    capsealEnd = models.IntegerField(default=0)
    expensesText = models.TextField(blank=True)
    supplyIns = models.TextField(blank=True)
    dutyText = models.TextField(blank=True)
    cashturnoverCalc = models.DecimalField(
        decimal_places=2, max_digits=10, default=0)
    cashturnoverRep = models.DecimalField(
        decimal_places=2, max_digits=10, default=0)
    cashtaken = models.DecimalField(decimal_places=2, max_digits=10, default=0)


class Labreport (models.Model):
    dateReport = models.DateField()
    dealer = models.IntegerField(default=0)
    less = models.IntegerField(default=0)
    pickup = models.IntegerField(default=0)
    smallText = models.IntegerField(default=0)
    goodly = models.IntegerField(default=0)
    square = models.IntegerField(default=0)
    rndgal = models.IntegerField(default=0)
    rndEnd = models.IntegerField(default=0)
    badgermeter = models.IntegerField(default=0)
    capsealEnd = models.IntegerField(default=0)
    squareSlEnd = models.IntegerField(default=0)
    supplyIns = models.TextField(blank=True)
    expensesText = models.TextField(blank=True)
    dutyText = models.TextField(blank=True)
    cashturnoverCalc = models.DecimalField(
        decimal_places=2, max_digits=10, default=0)
    cashturnoverRep = models.DecimalField(
        decimal_places=2, max_digits=10, default=0)
    cashtaken = models.DecimalField(decimal_places=2, max_digits=10, default=0)


class Kalimpreport (models.Model):
    dateReport = models.DateField()
    dealer = models.IntegerField(default=0)
    less = models.IntegerField(default=0)
    pickup = models.IntegerField(default=0)
    smallText = models.IntegerField(default=0)
    bakeryGal = models.IntegerField(default=0)
    square = models.IntegerField(default=0)
    smallSquare = models.IntegerField(default=0)
    rndgal = models.IntegerField(default=0)
    rndEnd = models.IntegerField(default=0)
    badgermeter = models.IntegerField(default=0)
    capsealEnd = models.IntegerField(default=0)
    squareSlEnd = models.IntegerField(default=0)
    supplyIns = models.TextField(blank=True)
    expensesText = models.TextField(blank=True)
    dutyText = models.TextField(blank=True)
    cashturnoverCalc = models.DecimalField(
        decimal_places=2, max_digits=10, default=0)
    cashturnoverRep = models.DecimalField(
        decimal_places=2, max_digits=10, default=0)
    cashtaken = models.DecimalField(decimal_places=2, max_digits=10, default=0)
