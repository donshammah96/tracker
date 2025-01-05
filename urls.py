from django.urls import path
from .views import ExpenseListCreate, IncomeListCreate, monthly_summary

urlpatterns = [
    # URL pattern for listing and creating expenses
    path('expenses/', ExpenseListCreate.as_view(), name='expense-list-create'),
    # URL pattern for listing and creating income
    path('income/', IncomeListCreate.as_view(), name='income-list-create'),
    # URL pattern for generating monthly summary
    path('summary/<int:year>/<int:month>/', monthly_summary, name='monthly-summary'),
]