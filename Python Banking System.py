all_accounts = []
import random
def open_account():
    account_title = input("Account Title:")
    cnic = input("CNIC: ")
    contact = input("Contact Number: ")
    initial_deposit = int(input("Initial Deposit: "))
    account_number = random.randint(10000, 99999)

    account = {
        'title':account_title,
        'cnic':cnic,
        'contact number':contact,
        'balance':initial_deposit,
        'account number':account_number
    }    
   
    all_accounts.append(account)
    print("Account Created Successfully")
    print(f"Your Account Title is {account['title']} and Account Number is {account['account number']}")

def cash_deposit(account_number, amount):
    if amount > 0:
        for acc in all_accounts:
            if acc['account number'] == account_number:
                acc['balance']+=amount
                print("Amount Deposited Successfully")
                break
        else:
            print("Invalid Account Number")
    else:
        print("Invalid Amount")

def check_balance(account_number):
    for acc in all_accounts:
            if acc['account number'] == account_number:
                print(f"Your account balance is Rs.{acc['balance']}")
                break
    else:
        print("Invalid Account Number")

def cash_withdrawl(account_number, amount):
    for acc in all_accounts:
        if (acc['account number'] == account_number) and (acc['balance'] >= amount):
            acc['balance']-=amount
            print(f"here is your amount Rs. {amount}")
            break
        else:
            print("Invalid Account Number")

def close_account(account_number):
    for i, acc in enumerate(all_accounts):
        if acc['account number'] == account_number:
            print(f"here is your amount Rs.{acc['balance']}")
            acc['balance'] = 0
            del all_accounts[i]
            print("Your Account is closed successfully")
            break
        else:
            print("Invalid Account Number")

while True:
    print("\n======= Welcome to Python Bank =======")
    print("1. Open Account")
    print("2. Deposit Cash")
    print("3. Withdraw Cash")
    print("4. Check Balance")
    print("5. Close Account")
    print("6. Exit")
    
    choice = input("Enter your choice (1–6): ")

    if choice == '1':
        open_account()
    
    elif choice == '2':
        acc_num = int(input("Enter your Account Number: "))
        amt = int(input("Enter amount to deposit: "))
        cash_deposit(acc_num, amt)

    elif choice == '3':
        acc_num = int(input("Enter your Account Number: "))
        amt = int(input("Enter amount to withdraw: "))
        cash_withdrawl(acc_num, amt)

    elif choice == '4':
        acc_num = int(input("Enter your Account Number: "))
        check_balance(acc_num)

    elif choice == '5':
        acc_num = int(input("Enter your Account Number: "))
        close_account(acc_num)

    elif choice == '6':
        print("Thank you for using Python Bank. Goodbye!")
        break

    else:
        print("Invalid choice. Please select from 1 to 6.")
