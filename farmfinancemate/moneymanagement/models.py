from django.db import models
from django.contrib.auth.models import User

# Create your models here
class FarmExpense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense_type = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.expense_type} - {self.amount} - {self.date}"

class FarmIncome(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income_type = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.income_type} - {self.amount} - {self.date}"
