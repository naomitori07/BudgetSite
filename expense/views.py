from django.shortcuts import render

def expense_list(request):
    return render(request, 'expense/expense_list.html', {})
