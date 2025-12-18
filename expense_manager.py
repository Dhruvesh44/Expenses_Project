import csv
import os
from datetime import datetime

class ExpenseManager:
    def __init__(self, filename="expenses.csv"):
        self.filename = filename
        # TODO: Initialize the CSV file with headers
        self.create_file()
    

    def create_file(self):
        """create a csv file with headers if it does noit exists"""
        if not os.path.exists(self.filename):
            #open file in write mode:
            with open(self.filename, "w", newline='') as file:
                #create a new CSV writer
                writer = csv.writer(file)
                #write the header row
                writer.writerow(["Date", "Amount", "Category", "Description"])

    
    def add_expense(self, amount, category, description=""):
        # TODO: Validate amount is positive number
        # TODO: Add expense to CSV with current date
        try:
            amount = float(amount)
            if amount > 0:
                date = datetime.now().strftime("%Y-%m-%d")
                with open(self.filename, "a", newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([date, amount, category, description])
                return True            
            else:
                print("amount must be positive!")
                return False
            
        except ValueError:
            print("you have not entered a number!")
            return False
        
    
    def view_expenses(self):
        with open(self.filename, "r") as f:
            reader = csv.reader(f)
            expenses = list(reader)

        if len(expenses) <= 1:
            return "No expenses have been recorded yet."  # RETURN instead of print

        # Build the result string
        result = "Your Expenses:\n"
        result += "-" * 50 + "\n"
        result += f"{'Date':<10} {'Amount':<10} {'Category':<15} {'Description':<20}\n"
        result += "-" * 50 + "\n"
        
        for expense in expenses[1:]:
            result += f"{expense[0]:<10} {expense[1]:<10} {expense[2]:<15} {expense[3]:<20}\n"
        
        return result  # RETURN the formatted string

            

        
    def show_summary(self):
        category_totals = {}
        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            expenses = list(reader)
        
        total = 0
        for i in expenses[1:]:
            total += float(i[1])
            if i[2] not in category_totals:
                category_totals[i[2]] = float(i[1])
            else:
                category_totals[i[2]] += float(i[1])
        
        # Build result string instead of printing
        result = f"Total Expenses: £{total:.2f}\n\n"
        result += "Spending by Category:\n"
        result += "-" * 30 + "\n"
        
        for category, category_total in category_totals.items():
            result += f"{category:<15} £{category_total:>8.2f}\n"
        
        result += "-" * 30 + "\n"
        result += f"{'Total':<15} £{total:>8.2f}"
        
        return result  # RETURN the string