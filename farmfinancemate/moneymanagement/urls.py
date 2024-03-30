from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('register', views.register_page, name='register'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),
    path('home', views.home, name='home'),
    path('farm_expense', views.farm_expense, name='farm_expense'),
    path('farm_income', views.farm_income, name='farm_income'),
    path('update_expense/<str:id>', views.update_expense, name='update_expense'),
    path('update_income/<str:id>', views.update_income, name='update_income'),
    path('delete_expense/<str:id>', views.delete_expense, name='delete_expense'),
    path('delete_income/<str:id>', views.delete_income, name='delete_income'),
]
