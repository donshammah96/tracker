from rest_framework import generics
from .models import Expense, Income
from .serializers import ExpenseSerializer, IncomeSerializer
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime

# View to list and create expenses
class ExpenseListCreate(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

# View to list and create income
class IncomeListCreate(generics.ListCreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

# View to generate monthly summary of expenses and income
@api_view(['GET'])
def monthly_summary(request, year, month):
    expenses = Expense.objects.filter(date__year=year, date__month=month).aggregate(Sum('amount'))
    income = Income.objects.filter(date__year=year, date__month=month).aggregate(Sum('amount'))
    summary = {
        'total_expenses': expenses['amount__sum'] or 0,
        'total_income': income['amount__sum'] or 0,
        'net_savings': (income['amount__sum'] or 0) - (expenses['amount__sum'] or 0)
    }
    return Response(summary)
