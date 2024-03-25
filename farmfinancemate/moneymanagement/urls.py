from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('register', views.register_page, name='register'),
    path('login', views.login_page, name='login'),
    path('add-expense', views.farm_expense, name='add-expense'),
    path('add-income', views.farm_income, name='add-income'),
]
