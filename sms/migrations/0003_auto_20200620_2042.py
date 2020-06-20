# Generated by Django 3.0.4 on 2020-06-20 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0002_auto_20200620_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='camelTirednes',
            field=models.IntegerField(default=0, verbose_name='Camel Tiredness'),
        ),
        migrations.AddField(
            model_name='game',
            name='canteen',
            field=models.IntegerField(default=3, verbose_name='Canteen'),
        ),
        migrations.AddField(
            model_name='game',
            name='done',
            field=models.BooleanField(default=False, verbose_name='Game Finished'),
        ),
        migrations.AddField(
            model_name='game',
            name='enemyTraveled',
            field=models.IntegerField(default=0, verbose_name='Enemy Traveled'),
        ),
        migrations.AddField(
            model_name='game',
            name='milesTraveled',
            field=models.IntegerField(default=0, verbose_name='Miles Traveled'),
        ),
        migrations.AddField(
            model_name='game',
            name='oasis',
            field=models.IntegerField(default=-1, verbose_name='Oasis Distance'),
        ),
        migrations.AddField(
            model_name='game',
            name='thirst',
            field=models.IntegerField(default=0, verbose_name='Thirst'),
        ),
    ]
