def add_expense(expenses, amount: float, category: str, label: str):
    expenses.append({"category": category, "amount": amount, "label": label})


def print_expenses(expenses):
    for expense in expenses:
        print(
            f"Name: {expense['label']} - Category: {
                expense['category']
            } - Amount: {expense['amount']}"
        )


def sum_expenses(expenses):
    return sum(map(lambda expense: expense["amount"], expenses))


def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense["category"] == category, expenses)


def main():
    expenses = []

    print("**Expense Tracker**")

    while True:
        print("1 - Add expense")
        print("2 - Print expenses")
        print("3 - Sum all expenses")
        print("4 - Filter expenses by category")
        print("5 - Quit")
        choice = input("\nPlease select your choice: ")

        if choice == "1":
            label = input("\nPlease insert a label of expense: ").capitalize()
            category = input(
                "\nPlease insert a category of expense: ").capitalize()
            amount = float(input("\nPlease insert the amount of expense: "))
            add_expense(expenses, amount, category, label)
        elif choice == "2":
            print_expenses(expenses)
        elif choice == "3":
            print("Total of expenses: ", sum_expenses(expenses))
        elif choice == "4":
            category = input("\nInsert the category to filter: ").capitalize()
            expenses_filtered = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_filtered)
        elif choice == "5":
            break
        else:
            print("Invalid choice")


main()
