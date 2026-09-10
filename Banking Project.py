import time  #Imports time in the sense of sleep
import datetime  #Import Time and date

def show_balance(balance):
    try:
            show = int(input("Please Enter your secret pin :"))
    except ValueError:
        print("Invalid input! Please Enter numbers only.")
        return 0
    if show == 1111:
        print(f"Available balance is ${balance}")
    else:
        print("Wrong pin")
        
def withdraw(balance):
    try:
        pin = int(input("Please Enter your secret pin :"))
    except ValueError:
        print("Invalid input! Please Enter numbers only.")
        return 0
    if pin == 1111 :
        withdraw_amount = int(input("Please Enter Amount "))
        if withdraw_amount > balance:
          print(f"Insufficient funds,Available balance is :$ {balance}")
          return 0
        elif withdraw_amount == balance:
          print(f"Sorry sir/mam You need to maintain minimum balance and Available balance is {balance}")
          return 0
        elif withdraw_amount < balance:
            print("Please Wait")
            time.sleep(1)
            print("Amount Withdrawed")
            Balance = input("Do You want to Check Available Balance(y/n)")
            Balance = Balance.lower()#it converts the input into small letters
            if Balance == 'y':
              print(f"Available Balance :${balance - withdraw_amount}")
              print("Thank You")
            else:
              print("Thank you")
        else:
            print("Incorrect pin")
        return withdraw_amount
    else:
        print("Try Again")
        return 0
        
def deposit(balance):
    try:
        pin = int(input("Please Enter your secret pin :"))
    except ValueError:
        print("Invalid input! Please Enter numbers only.")
        return 0
    if pin == 1111:
        amount = float(input("Enter your deposit amount: "))
        if amount <= 0:
            print("Invalid Amount")
            return 0
        else:
            return amount
    else:
        print("Incorrect Pin")
        return 0
        
def help():
    print("Please contact bank@gmail.com")
#date = datetime.datetime.now()
#print(date)

def main():
    balance = 5
    is_running = True
    while is_running:
        time.sleep(1)
        print("Welcome and Good Day")
        print("May i help you")
        print("1 = Showbalance ")
        print("2 = withdraw")
        print("3 = deposit  ") 
        print("4 = help   " )
        print("5 = Exit")
        choice = (input("Enter you choice from (1 - 5)"))
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance -= withdraw(balance)
        elif choice == '3':
            balance += deposit(balance)
        elif choice == '4':
            help()
        elif choice == '5':
            is_running = False
        else:
            print("It is an invalid choice please try again")
    print("Thank You")
    
if __name__ == '__main__':
    main()
