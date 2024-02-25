class Admin:
    def __init__(self, bank):
        self.bank = bank

    def check_accounts(self):
        self.bank.admin_check_accounts()

    def total_balance(self):
        self.bank.admin_total_balance()

    def toggle_loan(self):
        self.bank.loan_feature = not self.bank.loan_feature
        status = "enabled" if self.bank.loan_feature else "disabled"
        print(f"Loan feature is now {status}")
