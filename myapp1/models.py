from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    second_name = models.CharField(max_length=35, blank=False)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.pk} {self.name} {self.second_name} {self.salary} '


# Create your models here.
class Equipment(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    purchase_date = models.DateField(default='2020-01-01', blank=False)
    price = models.DecimalField(default=0.0, decimal_places=4, max_digits=10)

    def __str__(self):
        return f' {self.pk} {self.name} {self.price} {self.purchase_date}'
