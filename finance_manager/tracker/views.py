from django.shortcuts import render
from .models import Expense, Category

def index(request):
    expenses = Expense.objects.all()
    categories = Category.objects.all()
    return render(request, 'tracker/index.html', {'expenses': expenses, 'categories': categories})