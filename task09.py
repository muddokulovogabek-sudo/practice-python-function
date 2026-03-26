def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        print(" Mablag‘ yetarli emas")
        return balance
    return balance - amount

def check_balance(balance):
    print(f" Sizning balansingiz: {balance}")


balance = 1000.0

while True:
    choice = input("1-Deposit, 2-Withdraw, 3-Balance, 0-Chiqish: ")

    if choice == "1":
        amount = float(input("Summani kiriting: "))
        balance = deposit(balance, amount)

    elif choice == "2":
        amount = float(input("Summani kiriting: "))
        balance = withdraw(balance, amount)

    elif choice == "3":
        check_balance(balance)

    elif choice == "0":
        break

    else:
        print(" Noto‘g‘ri tanlov")