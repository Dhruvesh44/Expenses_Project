from expense_manager import ExpenseManager

def main():
    manager = ExpenseManager()
    
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Summary")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        

        if choice == "1":
            amount = input("enter amount: ")
            cat = input("enter category: ")
            des = input("enter a description: ")
            res = manager.add_expense(amount, cat, des)
            if res: 
                print("successfully added the expense")
            else:
                print("error: failed to add expense, please check amount is a valid number")
    
        elif choice == "2":
            # TODO: Call manager.view_expenses()
            manager.view_expenses()
            
        elif choice == "3":
            # TODO: Call manager.show_summary()
            manager.show_summary()
            
        elif choice == "4":
            print("Goodbye!")
            break  # This exits the while loop
            
        #else:
            print("Invalid option. Please choose 1-4.")



if __name__ == "__main__":
    main()