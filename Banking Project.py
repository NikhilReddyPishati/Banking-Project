#Banking project
import time  #Imports time in the sense of sleep
import datetime  #Import Time and date
def show_balance():    #This is the new function
    show=int(input("please enter your secret 4 digit pin"))  #Print the statements
    if show == pin:     #this compares input and pin
        print(f"Available balance is ${balance}")   #Print Statements
    else:   #Else condition 
        print("wrong pin")  
def withdraw():     #New Function
    withdraw_amount=int(input("please enter amount "))   
    if withdraw_amount > balance:   #compares the difference 
        print(f"Insufficient funds available balance is {balance}").  #Prints Insufficient Funds
    elif withdraw_amount == balance:  #Again Compares the Value
        print(f"sorry sir/mam You need to maintain minimum balance and Available balance is {balance}") #Prints
    elif withdraw_amount < balance: #Again compares
        pin = int(input("please enter your secret pin :")) #If condition is true follows
        if pin == pin:  #Pin is previously Stored And Compares it
            print(f"Amount withdrawed and available balance is:${balance-withdraw_amount}")
        else:
            print(f"Incorrect pin please start the process again")
def deposit():
    deposit_money = int(input("Please Enter the amount you want to deposit :$ "))
    pin = int(input("please enter your secret pin "))
    if pin == 0000: #This is the 
            print(f"Amount deposited and available balance is:${balance+deposit_money}")
    else:
        print("Incorrect pin please start the process again")
def help():
    print("please contact bank@gmail.com")
date =datetime.datetime.now()
print(date)
balance = 5
pin = 0000
is_running = True
while is_running:
    time.sleep(1)
    print("welcome and Good Day")
    print("May i help you")
    print("1 = Showbalance ")
    print("2 = withdraw")
    print("3 = deposit  ") 
    print("4 = help   " )
    print("5 = Exit")
    choice = (input("Enter you choice from (1 - 5)"))
    if choice == '1':
        show_balance()
    elif choice == '2':
        withdraw()
    elif choice == '3':
        deposit()
    elif choice == '4':
        help()
    elif choice == '5':
        is_running = False
    else:
        print("it is an invalid choice please try again")
print("Thank You")


def show_balance(balance):
    show=int(input("please enter your secret 4 digit pin"))
    if show == 0000:
        print(f"Available balance is ${balance}")
    else:
        print("wrong pin")
def withdraw(balance):
    withdraw_amount=float(input("please enter amount "))
    if withdraw_amount > balance:
        print(f"Insufficient funds available balance is {balance}")
    elif withdraw_amount == balance:
        print(f"sorry sir/mam You need to maintain minimum balance and Available balance is {balance}")
    elif withdraw_amount < balance:
        pin = int(input("please enter your secret pin :"))
        if pin == 0000 :
            print(f"Amount withdrawed and available balance is:${balance-withdraw_amount}")
        else:
            return withdraw_amount
def deposit(balance):
    amount = float(input("enter your deposit amount"))
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
        #time.sleep(1)
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
            balance -=withdraw(balance)
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
