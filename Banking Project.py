
import time  #Imports time in the sense of sleep
import datetime  #Import Time and date

def show_balance(balance):
    show=int(input("please enter your secret 4 digit pin: "))
    if show == 0000:
        print(f"Available balance is ${balance}")
    else:
        print("wrong pin")
def withdraw(balance):
    pin = int(input("please enter your secret pin :"))
    if pin == 0000 :
        withdraw_amount = int(input("please enter amount "))
        if withdraw_amount > balance:
          print(f"Insufficient funds available balance is {balance}")
        elif withdraw_amount == balance:
          print(f"sorry sir/mam You need to maintain minimum balance and Available balance is {balance}")
        elif withdraw_amount < balance:
            print(f"Amount withdrawed and available balance is:${balance-withdraw_amount}")
        else:
            print("Incorrect pin")
        return withdraw_amount
    else:
        print("Try Again")
def deposit(balance):
    pin=int(input("Please Enter Your Pin"))
    if pin == 0000:
        amount = float(input("enter your deposit amount: "))
    if amount <= 0:
        print("invalid amount")
        return 0
    else:
        return amount
def help():
    print("please contact bank@gmail.com")
#date =datetime.datetime.now()
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
            print("it is an invalid choice please try again")
    print("Thank You")
    
if __name__ == '__main__':
    main()
