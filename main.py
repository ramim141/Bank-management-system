from Bank import Bank
from Customer import Customer
from Admin import Admin

class Main:
    def __init__(self):
        self.bank = Bank()
        self.customer = Customer(self.bank)
        self.admin = Admin(self.bank)

    def run(self):
        print("-----Welcome to the PhitronBank--------")

        while True:
            print("\n1. Customer Menu")
            print("2. Admin Menu")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.user_menu()

            elif choice == '2':
                self.admin_menu()

            elif choice == '3':
                print("Thank you for using the Bank Management System.")
                break

            else:
                print("Invalid choice. Please enter a valid option.")

    def user_menu(self):
        print("\nUser Menu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transfer")
        print("6. Take Loan")
        print("7. Check Transactions")
        print("8. Exit User Menu")
        user_choice = input("Enter your choice: ")

        if user_choice == '1':
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            account_type = input("Enter account type (Savings/Current): ").capitalize()
            self.customer.create_account(name, email, address, account_type)

        elif user_choice == '2':
            account_number = int(input("Enter your account number: "))
            amount = float(input("Enter amount to deposit: "))
            self.customer.deposit(account_number, amount)

        elif user_choice == '3':
            account_number = int(input("Enter your account number: "))
            amount = float(input("Enter amount to withdraw: "))
            self.customer.withdraw(account_number, amount)

        elif user_choice == '4':
            account_number = int(input("Enter your account number: "))
            self.customer.check_balance(account_number)

        elif user_choice == '5':
            from_account = int(input("Enter your account number: "))
            to_account = int(input("Enter recipient's account number: "))
            amount = float(input("Enter amount to transfer: "))
            self.customer.transfer_balance(from_account, to_account, amount)

        elif user_choice == '6':
            account_number = int(input("Enter your account number: "))
            amount = float(input("Enter loan amount: "))
            self.customer.loan(account_number, amount)

        elif user_choice == '7':
            account_number = int(input("Enter your account number: "))
            self.customer.check_transaction(account_number)

        elif user_choice == '8':
            return

        else:
            print("Invalid choice. Returning to main menu.")

    def admin_menu(self):
        print("\nAdmin Menu:")
        print("1. Check All Accounts")
        print("2. Check Total Balance")
        print("3. Toggle Loan Feature")
        print("4. Exit Admin Menu")
        admin_choice = input("Enter your choice: ")

        if admin_choice == '1':
            self.admin.check_accounts()

        elif admin_choice == '2':
            self.admin.total_balance()

        elif admin_choice == '3':
            self.admin.toggle_loan()

        elif admin_choice == '4':
            return

        else:
            print("Invalid choice. Returning to main menu.")


if __name__ == "__main__":
    main = Main()
    main.run()
