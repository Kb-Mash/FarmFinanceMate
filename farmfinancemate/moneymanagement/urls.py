from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('register', views.register_page, name='register'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),
    path('home', views.home, name='home'),
    path('add-expense', views.farm_expense, name='add-expense'),
    path('add-income', views.farm_income, name='add-income'),
    path('edit_expense/<str:id>', views.update_expense, name='edit_expense'),
    path('edit_income/<str:id>', views.update_income, name='edit_income'),
    path('delete_income/<str:id>', views.delete_expense, name='delete_expense'),
    path('delete_income/<str:id>', views.delete_income, name='delete_income'),
]
