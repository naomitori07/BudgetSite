# Generated by Django 2.0.8 on 2018-08-27 21:54

from django.db import migrations, models
import expense.models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0003_auto_20180828_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[(expense.models.Category('Food'), 'Food'), (expense.models.Category('Eating Out'), 'Eating Out'), (expense.models.Category('Monthly Bills'), 'Monthly Bills'), (expense.models.Category('Yearly'), 'Yearly'), (expense.models.Category('Extra'), 'Extra'), (expense.models.Category('Transportation'), 'Transportation'), (expense.models.Category('Out'), 'Out')], max_length=200),
        ),
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='expense',
            name='explanation',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='expense',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
