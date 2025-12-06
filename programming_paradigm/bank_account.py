class BankAccount:
    def __init__(self, balance=0.0):
        """Initialize the bank account with a starting balance."""
        self.balance = balance

    def deposit(self, amount):
        """Add money to the account and print the deposited amount."""
        self.balance += amount
        print(f"Deposited: ${amount}")

    def withdraw(self, amount):
        """Withdraw money if funds are available; otherwise show an error."""
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        """Print the current account balance with two decimal places."""
        print(f"Current Balance: ${self.balance:.2f}")
