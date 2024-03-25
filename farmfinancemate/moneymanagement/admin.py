from django.contrib import admin
from .models import FarmExpense, FarmIncome

# Register your models here.
admin.site.register(FarmExpense)
admin.site.register(FarmIncome)
