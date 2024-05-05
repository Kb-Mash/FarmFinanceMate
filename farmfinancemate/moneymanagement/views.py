from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.db.models import Sum
from .models import FarmExpense, FarmIncome, ExpenseCategory, IncomeCategory
from datetime import datetime

# Create your views here.


def base(request):
    """
    View function for the base template

    Args:
        request: HttpRequest object

    Retuns:
        HttpResponse object
    """
    return render(request, 'base.html')


def register_page(request):
    """
    View function for user registration

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse object or redirect object
    """
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


def login_page(request):
    """
    View function for user registration

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse object or redirect object
    """
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


@login_required
def logout_page(request):
    """
    View function for user registration

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse object or redirect object
    """
    auth.logout(request)
    return redirect('/')

# home page
@login_required
def home(request):
    """
    View function for user registration

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse object or redirect object
    """
    return render(request, 'home.html')


@login_required
def expense_category(request):
    if not ExpenseCategory.objects.exists():
        ExpenseCategory.create_predefined_categories()

    queryset = ExpenseCategory.objects.all() #.order_by('category')
    context = {'categories': queryset}
    
    return render(request, 'expense_category.html', context)


@login_required
def income_category(request):
    if not IncomeCategory.objects.exists():
        IncomeCategory.create_predefined_categories()

    queryset = IncomeCategory.objects.all() #.order_by('category')
    context = {'categories': queryset}
    
    return render(request, 'income_category.html', context)

@login_required
def farm_expense(request, id):
    """
    View function for user registration

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse object or redirect object
    """
    category = ExpenseCategory.objects.get(id=id)

    if request.method == 'POST':
        expense = request.POST.get('expense')
        amount = request.POST.get('amount')
        user_date = request.POST.get('user_date')

        if expense and amount and user_date:
            expense = FarmExpense.objects.create(user=request.user, category=category, expense=expense, amount=amount, user_date=user_date)
            messages.success(request, 'Farm expense added successfully')
            return redirect('farm_expense', id=id)
        else:
            messages.error(request, 'Fill in the information')
            return redirect('farm_expense', id=id)

    queryset = FarmExpense.objects.all()

    total_sum = queryset.aggregate(total_amount=Sum('amount'))['total_amount'] or 0

    context = {'category': category, 'expenses': queryset, 'total_sum': total_sum}
    return render(request, 'farm_expense.html', context)


@login_required
def farm_income(request, id):
    """
    View function for user registration

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse object or redirect object
    """
    category = IncomeCategory.objects.get(id=id)

    if request.method == 'POST':
        income = request.POST.get('income')
        amount = request.POST.get('amount')
        user_date = request.POST.get('user_date')

        if income and amount and user_date:
            income = FarmIncome.objects.create(user=request.user, category=category, income=income, amount=amount, user_date=user_date)
            messages.success(request, 'Farm income added successfully')
            return redirect('farm_income', id=id)
        else:
            messages.error(request, 'Fill in the information')
            return redirect('farm_income', id=id)

    queryset = FarmIncome.objects.all()

    total_sum = queryset.aggregate(total_amount=Sum('amount'))['total_amount'] or 0

    context = {'category': category, 'incomes': queryset, 'total_sum': total_sum}
    return render(request, 'farm_income.html', context)


@login_required
def update_expense(request, id):
    """
    View function for user registration

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse object or redirect object
    """
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


@login_required
def update_income(request, id):
    """
    View function for user registration

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse object or redirect object
    """
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


@login_required
def delete_expense(request, id):
    """
    View function for user registration

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse object or redirect object
    """
    queryset = FarmExpense.objects.get(id=id)
    queryset.delete()
    messages.success(request, 'Expense deleted successfully.')
    return redirect('farm_expense')


@login_required
def delete_income(request, id):
    """
    View function for user registration

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse object or redirect object
    """
    queryset = FarmIncome.objects.get(id=id)
    queryset.delete()
    messages.success(request, 'Income deleted successfully.')
    return redirect('farm_income')
