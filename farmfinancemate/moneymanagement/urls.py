from django.urls import path
from . import views

# URL patterns for the moneymanagement app

urlpatterns = [
    path('', views.base, name='base'),
    path('register', views.register_page, name='register'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),
    path('home', views.home, name='home'),
    path('expense_category', views.expense_category, name='expense_category'),
    path('income_category', views.income_category, name='income_category'),
    path('farm_expense/<str:id>', views.farm_expense, name='farm_expense'),
    path('farm_income/<str:id>', views.farm_income, name='farm_income'),
    path('update_expense/<str:id>', views.update_expense, name='update_expense'),
    path('update_income/<str:id>', views.update_income, name='update_income'),
    path('delete_expense/<str:id>', views.delete_expense, name='delete_expense'),
    path('delete_income/<str:id>', views.delete_income, name='delete_income'),
]
