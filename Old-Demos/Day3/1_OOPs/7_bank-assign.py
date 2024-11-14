from abc import ABC, abstractmethod

# Step 1: Define Notification Interfaces
class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class SMSNotifier(Notifier):
    def send(self, message: str):
        print(f"SMS Notification: {message}")

class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"Email Notification: {message}")

# Step 2: BankAccount Class that Adheres to SOLID Principles
class BankAccount:
    def __init__(self, initial_balance: float, notifiers: list[Notifier]):
        self._balance = initial_balance
        self._notifiers = notifiers  # List of notifiers (SMS, Email, etc.)

    def deposit(self, amount: float):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self._balance += amount
        self._notify(f"Deposit of {amount} successful. Current balance: {self._balance}")

    def withdraw(self, amount: float):
        if amount > self._balance:
            print("Error: Insufficient funds.")
            self._notify("Withdrawal attempt failed due to insufficient funds.")
            return
        self._balance -= amount
        self._notify(f"Withdrawal of {amount} successful. Current balance: {self._balance}")

    def _notify(self, message: str):
        for notifier in self._notifiers:
            notifier.send(message)

    @property
    def balance(self):
        return self._balance

# Step 3: Usage Example
if __name__ == "__main__":
    # Instantiate notifiers
    sms_notifier = SMSNotifier()
    email_notifier = EmailNotifier()

    # Create a bank account with an initial balance and notifiers
    account = BankAccount(initial_balance=1000, notifiers=[sms_notifier, email_notifier])

    # Perform some transactions
    account.deposit(500)       # Deposit 500
    account.withdraw(200)      # Withdraw 200
    account.withdraw(1500)     # Attempt to withdraw more than balance
