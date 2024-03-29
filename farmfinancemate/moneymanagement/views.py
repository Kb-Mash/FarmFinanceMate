from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.db.models import Sum
from .models import FarmExpense, FarmIncome

# Create your views here.

# base page for the app
def base(request):
    """
    This function renders the base page

    Args:
        request: request object

    Returns:
        render: renders the base page
    """
    return render(request, 'base.html')

# register page for user registration
def register_page(request):
    """
    This function registers a user

    Args:
        request: request object

    Returns:
        render: renders the register page if the request method is GET, else redirects to login page
    """
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'Username already exists')
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password1, email=email, first_name=firstname, last_name=lastname)
                    user.save()
                    messages.success(request, 'User created successfully')
                    return redirect('login')
            except Exception as e:
                messages.error(request, 'Error creating user')
                return redirect('register')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    return render(request, 'register.html')

# login page for user login
def login_page(request):
    """
    This function logs in a user

    Args:
        request: request object

    Returns:
        render: renders the login page if the request method is GET, else redirects to home page
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('home')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('login')
        except Exception as e:
            messages.error(request, 'Error logging in')
            return redirect('login')
    return render(request, 'login.html')

# logout view
@login_required
def logout_page(request):
    """
    This function logs out a user

    Args:
        request: request object

    Returns:
        redirect: redirects to home page
    """
    auth.logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('base')

# home page for the app
@login_required(login_url='/login/')
def home(request):
    """
    This function renders the home page

    Args:
        request: request object

    Returns:
        render: renders the home page
    """
    return render(request, 'home.html')

# farm expense page for adding farm expenses
@login_required
def farm_expense(request):
    """
    This function adds farm expenses

    Args:
        request: request object

    Returns:
        render: renders the farm expense page if the request method is GET, else redirects to home page
    """
    if request.method == 'POST':
        # Handling form submission to add a new farm expense
        expense_type = request.POST.get('expense_type')
        amount = request.POST.get('amount')
        if expense_type and amount:
            try:
                expense = FarmExpense.objects.create(user=request.user, expense_type=expense_type, amount=amount)
                messages.success(request, 'Farm expense added successfully')
                return redirect('farm_expense')
            except Exception as e:
                messages.error(request, 'Error adding farm expense')

    # Fetching all farm expenses from the database
    queryset = FarmExpense.objects.all()

    # Filtering expenses based on search query
    search_query = request.GET.get('search')
    if search_query:
        queryset = queryset.filter(expense_type__icontains=search_query)

    # Calculating total sum of expenses
    total_sum = queryset.aggregate(total_amount=Sum('amount'))['total_amount'] or 0

    context = {'expenses': queryset, 'total_sum': total_sum}

    return render(request, 'expenses.html', context)



# farm income page for adding farm incomes
@login_required
def farm_income(request):
    """
    This function adds farm incomes

    Args:
        request: request object

    Returns:
        render: renders the farm income page if the request method is GET, else redirects to home page
    """
    if request.method == 'POST':
        # Handling form submission to add a new farm income
        income_type = request.POST.get('income_type')
        amount = request.POST.get('amount')
        if income_type and amount:
            try:
                income = FarmIncome.objects.create(user=request.user, income_type=income_type, amount=amount)
                messages.success(request, 'Farm income added successfully')
                return redirect('farm_income')
            except Exception as e:
                messages.error(request, 'Error adding farm income')

    # Fetching all farm income from the database
    queryset = FarmIncome.objects.all()

    # Filtering income based on search query
    search_query = request.GET.get('search')
    if search_query:
        queryset = queryset.filter(income_type__icontains=search_query)

    # Calculating total sum of income
    total_sum = queryset.aggregate(total_amount=Sum('amount'))['total_amount'] or 0

    context = {'incomes': queryset, 'total_sum': total_sum}

    return render(request, 'income.html', context)

# update the Expenses data
@login_required
def update_expense(request, id):
    """
    View function for updating a farm expense.
    """
    expense = FarmExpense.objects.get(id=id)

    if request.method == 'POST':
        # Handling form submission to update the expense
        expense_type = request.POST.get('expense_type')
        amount = request.POST.get('amount')
        if expense_type and amount:
            try:
                expense.expense_type = expense_type
                expense.amount = amount
                expense.save()
                messages.success(request, 'Farm expense updated successfully')
                return redirect('farm_expense')
            except Exception as e:
                messages.error(request, 'Error updating farm expense')
                return redirect('update_expense')

    context = {'expense': expense}
    return render(request, 'update_expense.html', context)

# delete th Expense data
@login_required
def delete_expense(request, id):
    """
    View function for deleting a farm expense.
    """
    queryset = FarmExpense.objects.get(id=id)
    queryset.delete()
    return redirect('farm_expense')

# update the Income data
@login_required
def update_income(request, id):
    """
    View function for updating a farm income.
    """
    income = FarmIncome.objects.get(id=id)

    if request.method == 'POST':
        # Handling form submission to update the income
        income_type = request.POST.get('income_type')
        amount = request.POST.get('amount')
        if income_type and amount:
            try:
                income.income_type = income_type
                income.amount = amount
                income.save()
                messages.success(request, 'Farm income updated successfully')
                return redirect('farm_income')
            except Exception as e:
                messages.error(request, 'Error updating farm income')
                return redirect('update_income', id=id)

    context = {'income': income}
    return render(request, 'update_income.html', context)

# delete the Income data
@login_required
def delete_income(request, id):
    """
    View function for deleting a farm income.
    """
    queryset = FarmIncome.objects.get(id=id)
    queryset.delete()
    messages.success(request, 'Farm income deleted successfully')
    return redirect('farm_income')

@login_required
def home(request):
    """
    View function for the home page.
    """
    return render(request, 'home.html')
