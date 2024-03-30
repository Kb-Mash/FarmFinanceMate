from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.db.models import Sum
from .models import FarmExpense, FarmIncome

# Create your views here.

# base page for the app
def base(request):
    return render(request, 'base.html')

# register page for user registration
def register_page(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstname')
        lastName = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists.')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=firstName, last_name=lastName)
                user.save()
                messages.success(request, 'User created succesfully.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

    return render(request, 'register.html')

# login page for user login
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')
    return render(request, 'login.html')

# logout view
@login_required
def logout_page(request):
    auth.logout(request)
    return redirect('/')

# home page
@login_required
def home(request):
    return render(request, 'home.html')

# farm expense page for adding and viewing farm expenses
@login_required
def farm_expense(request):
    if request.method == 'POST':
        expense_type = request.POST.get('expense_type')
        amount = request.POST.get('amount')

        if expense_type and amount:
            expense = FarmExpense.objects.create(user=request.user, expense_type=expense_type, amount=amount)
            messages.success(request, 'Farm expense added successfully')
            return redirect('farm_expense')
        else:
            messages.error(request, 'Fill in the information')
            return redirect('farm_expense')

    queryset = FarmExpense.objects.all()

    total_sum = queryset.aggregate(total_amount=Sum('amount'))['total_amount'] or 0

    context = {'expenses': queryset, 'total_sum': total_sum}
    return render(request, 'farm_expense.html', context)

# farm income page for adding and viewing farm income
@login_required
def farm_income(request):
    if request.method == 'POST':
        income_type = request.POST.get('income_type')
        amount = request.POST.get('amount')

        if income_type and amount:
            income = FarmIncome.objects.create(user=request.user, income_type=income_type, amount=amount)
            messages.success(request, 'Farm income added successfully')
            return redirect('farm_income')
        else:
            messages.error(request, 'Fill in the information')
            return redirect('farm_income')

    queryset = FarmIncome.objects.all()

    total_sum = queryset.aggregate(total_amount=Sum('amount'))['total_amount'] or 0

    context = {'items': queryset, 'total_sum': total_sum}
    return render(request, 'farm_income.html', context)


# update the Expense data
@login_required
def update_expense(request, id):
    expense = FarmExpense.objects.get(id=id)

    if request.method == 'POST':
        expense_type = request.POST.get('expense_type')
        amount = request.POST.get('amount')

        if expense_type and amount:
            expense.expense_type = expense_type
            expense.amount = amount
            expense.save()
            messages.success(request, 'Farm expense updated successfully')
            return redirect('farm_expense')
        else:
            messages.error(request, 'Fill in the information')
            return redirect('update_expense')

    context = {'expense': expense}
    return render(request, 'update_expense.html', context)

# update the Income data
@login_required
def update_income(request, id):
    income = FarmIncome.objects.get(id=id)

    if request.method == 'POST':
        income_type = request.POST.get('income_type')
        amount = request.POST.get('amount')

        if income_type and amount:
            income.income_type = income_type
            income.amount = amount
            income.save()
            messages.success(request, 'Farm income updated successfully')
            return redirect('farm_income')
        else:
            messages.error(request, 'Fill in the information')
            return redirect('update_income')

    context = {'income': income}
    return render(request, 'update_income.html', context)

# delete the Expense data
@login_required
def delete_expense(request, id):
    queryset = FarmExpense.objects.get(id=id)
    queryset.delete()
    messages.success(request, 'Expense deleted successfully.')
    return redirect('farm_expense')

# delete the Income data
@login_required
def delete_income(request, id):
    queryset = FarmIncome.objects.get(id=id)
    queryset.delete()
    messages.success(request, 'Income deleted successfully.')
    return redirect('farm_income')
