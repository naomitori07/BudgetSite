from django.db import models
from django.utils import timezone
from enum import Enum


class Category(Enum):
    FOOD = "Food"
    EATING_OUT = "Eating Out"
    MONTHLY_BILLS = "Monthly Bills"
    YEARLY = "Yearly"
    EXTRA = "Extra"
    TRANSPORTATION = "Transportation"
    OUT = "Out"

    @classmethod
    def all(self):
        return [Category.FOOD,
                Category.EATING_OUT,
                Category.MONTHLY_BILLS,
                Category.YEARLY,
                Category.TRANSPORTATION,
                Category.EXTRA,
                Category.OUT,
               ]


class Expense(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=[(tag.value, tag.name) for tag in Category.all()])
    explanation = models.CharField(max_length=200)
    date = models.DateTimeField()
    amount = models.DecimalField(decimal_places=2, max_digits=10)

    def publish(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Budget(models.Model):
    updated = models.DateTimeField(default = timezone.now)
    category = models.CharField(max_length=200, choices=[(tag.value, tag.name) for tag in Category.all()])
    amount = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.category
