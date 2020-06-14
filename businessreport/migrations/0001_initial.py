# Generated by Django 3.0.6 on 2020-05-24 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Labreport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateReport', models.DateField()),
                ('dealer', models.IntegerField(default=0)),
                ('less', models.IntegerField(default=0)),
                ('pickup', models.IntegerField(default=0)),
                ('smallText', models.IntegerField(default=0)),
                ('goodly', models.IntegerField(default=0)),
                ('square', models.IntegerField(default=0)),
                ('rndgal', models.IntegerField(default=0)),
                ('rndEnd', models.IntegerField(default=0)),
                ('badgermeter', models.IntegerField(default=0)),
                ('capsealEnd', models.IntegerField(default=0)),
                ('squareSlEnd', models.IntegerField(default=0)),
                ('expensesText', models.TextField(blank=True)),
                ('dutyText', models.TextField(blank=True)),
                ('cashturnoverCalc', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('cashturnoverRep', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('cashtaken', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Tmbreport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateReport', models.DateField()),
                ('dealer', models.IntegerField(default=0)),
                ('pickup', models.IntegerField(default=0)),
                ('rndgal', models.IntegerField(default=0)),
                ('rndEnd', models.IntegerField(default=0)),
                ('badgermeter', models.IntegerField(default=0)),
                ('capsealEnd', models.IntegerField(default=0)),
                ('expensesText', models.TextField(blank=True)),
                ('dutyText', models.TextField(blank=True)),
                ('cashturnoverCalc', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('cashturnoverRep', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('cashtaken', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
            ],
        ),
    ]
