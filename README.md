Python Bank Management System
This is a simple console-based Bank Management System built with Python.
It allows users to create bank accounts, deposit and withdraw money, check balances, and close accounts — all in one interactive menu.

📌 Features
Open Account → Create a new bank account with an initial deposit.

Deposit Cash → Add money to your account.

Withdraw Cash → Withdraw money if your balance is sufficient.

Check Balance → View your current account balance.

Close Account → Delete your account and withdraw the remaining balance.

Interactive Menu → Easy-to-use console interface.

🛠️ How It Works
The program stores all accounts in a list of dictionaries.

Each account contains:

Account Title

CNIC

Contact Number

Balance

Account Number (auto-generated randomly)

The menu runs in a while True loop until the user chooses to exit.

Functions handle specific operations:

open_account() → Creates a new account

cash_deposit(account_number, amount) → Adds funds

cash_withdrawl(account_number, amount) → Withdraws funds

check_balance(account_number) → Shows balance

close_account(account_number) → Deletes account
