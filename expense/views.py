from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Expense
from .forms import ExpenseForm
from django.utils import timezone
from django.db import transaction
from datetime import datetime
import time

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expense/expense_list.html', {'expenses': expenses})

def expense_detail(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    return render(request, 'expense/expense_detail.html', {'expense': expense})

def expense_new(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.save()
            return redirect('expense_detail', pk=expense.pk)
    else:
        form = ExpenseForm()
    return render(request, 'expense/expense_edit.html', {'form': form})

def expense_edit(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.save()
            return redirect('expense_detail', pk=expense.pk)
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expense/expense_edit.html', {'form': form})

def expense_upload(request):
	csv_file = request.FILES["csv_file"]
	file_data = csv_file.read().decode("utf-8")
	lines = file_data.split("\n")
	with transaction.atomic():
		for line in lines:
			fields = line.split(",")
			data_dict = {}
			data_dict["date"] = datetime.strptime(fields[0], "%d/%m/%y")
			data_dict["title"] = fields[1]
			data_dict["amount"] = fields[2]
			data_dict["category"] = fields[3]
			data_dict["explanation"] = fields[4]
			form = ExpenseForm(data_dict)
			if form.is_valid():
				form.save()
			else:
				print(form.errors)

	return redirect('expense_list')
