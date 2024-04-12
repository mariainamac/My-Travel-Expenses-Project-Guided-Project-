#Creating my expenses list

my_expenses_list = []

#Create a function to Add my expenses (item & amount)
def add_expense(item, amount):
    global my_expenses_list
    my_expenses_list.append((item, amount))

#Display the items and cost after saving the details to the list
def display_expenses ():
    global my_expenses_list
    for item, amount in my_expenses_list:
        print(f"{item}: {amount}")
    total_expenses = sum(amount for item, amount in my_expenses_list)
    print(f"Total expenses: {total_expenses}")

# Main logic of the project
def main():
    global my_expenses_list
    while True:
        print("\n1. Add my travel expenses")
        print("2. View my travel expenses")
        print("3. Exit")

        user_choice = input("\nWhat do you want to do today? ")

        if user_choice == '1':
            item = input("My Item: ")
            amount = float(input("Item Amount: "))
            add_expense(item, amount)
            print("Your travel expenses has been updated!")
        elif user_choice == '2':
            print("My travel expenses are: ")
            display_expenses()
        elif user_choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
