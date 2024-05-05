from django.db import models
from django.contrib.auth.models import User

# Create your models here
class ExpenseCategory(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.category}"

    @classmethod
    def create_predefined_categories(cls):
        categories = ['Seed', 'Seedlings', 'Fertilizers', 'Pesticides', 'Labour', 'Vet', 'Machinery', 'Others']
        cls.objects.bulk_create([cls(category=category) for category in categories])

#ExpenseCategory.create_predefined_categories()

class IncomeCategory(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.category}"
    
    @classmethod
    def create_predefined_categories(cls):
        categories = ['Crop Sale', 'Livestock Sale', 'Debtors', 'Government subsidies', 'Others']
        cls.objects.bulk_create([cls(category=category) for category in categories])

#ncomeCategory.create_predefined_categories()

class FarmExpense(models.Model):
    """
    Model class for farm expenses
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE, default=None)
    expense = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user_date = models.DateField(default=None)
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        """ string representation of the model instance """
        return f"{self.expense} - {self.amount} - {self.creation_date}"

class FarmIncome(models.Model):
    """
    Model class for farm income
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE, default=None)
    income = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user_date = models.DateField(default=None)
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        """ string representation of the model instance """
        return f"{self.income} - {self.amount} - {self.creation_date}"
