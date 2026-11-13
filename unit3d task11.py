balance = 1000

def deposit(amount):
    global balance
    balance += amount
    print("Deposited:", amount)

def show_balance():
    balance = 500
    print("Local Balance:", balance)

deposit(500)
show_balance()

print("Account Balance:", balance)