import statistics
import math
# Python program that analyzes a series of personl expenses
expense_list =[]
small_expense = 0
moderate_expense = 0
large_expense = 0
# ask for the first expense, tell user to enter 0 as expense when finished, create a list
expense = float(input("\nEnter your first expense (enter 0 when finished): "))

# verify the input is valid
# while the input is valid and not 0, append expenses to the list, 
# sort into expense size
# <25 = small expense
# 25-100 = medium expense
# >100 = large expense

while expense != 0 :
    if expense < 0 :
        expense = float(input("\nExpenses cannot be negative. Enter another expense: "))
    elif expense > 0 :
        expense_list.append(expense)
        if expense < 25 :
            small_expense += 1
        elif expense <= 100 :
            moderate_expense += 1
        else :
            large_expense +=1
        expense = float(input("\nEnter Your next expense (enter 0 when finished): "))

# print out:
# Total expenses
# average expense
# smallest expnese
# largest expense
# number of each size of expense
total_expenses = len(expense_list)
sum_expenses = math.fsum(expense_list)
average_expense = statistics.mean(expense_list)
max_expense = max(expense_list)
min_expense = min(expense_list)

print(f"""\nExpense Summary\n
Number of expenses: {total_expenses}
Total: ${sum_expenses:,.2f}
Average: ${average_expense:,.2f} 
Largest: ${max_expense:,.2f}
Smallest: ${min_expense:,.2f}\n
Small Expenses: {small_expense}
Moderate Expenses: {moderate_expense}
Large Expenses: {large_expense} """)
