from django.contrib import admin
from .models import FarmExpense, FarmIncome, ExpenseCategory, IncomeCategory

# Register your models here.
admin.site.register(ExpenseCategory)
admin.site.register(IncomeCategory)
admin.site.register(FarmExpense)
admin.site.register(FarmIncome)
