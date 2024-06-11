print("Welcome to the app of Infinite Money Bank")
print("Please type in the command of your chosen transaction below [1-4]")

print("==================================================")

print("[1] Check Balance")
print("[2] Withdraw Money")
print("[3] Deposit Money")
print("[4] Exit Application")

print("==================================================")

balance= 100.0

while True:
    command= int(input("Please enter your command:"))
 
    match command:
        case 1:
            print(f"Your current balance is: {balance} PHP")
        
        case 2:
            while True:
                withdraw= float(input("Please enter the amount you would like to withdraw:"))
                if withdraw<=balance and withdraw>0:
                    print(f"You have withdrawn an amount of {withdraw} PHP")
                    balance-=withdraw
                    print(f"Your current balance is {balance} PHP")
                    break
                elif withdraw>balance:
                    print("Insufficient Balance. Please try again.")
                elif withdraw<=0:
                    print("Invalid Amount. Please try again.")
                else:
                    pass
        
        case 3:
            while True:
                deposit= float(input("Please enter the amount you would like to deposit:"))
                if deposit>0:
                    print (f"You have deposited an amount of {deposit} PHP")
                    balance += deposit
                    print(f"Your current balance is {balance} PHP")
                    break
                elif deposit<=0:
                    print ("Invalid Amount. PLease try again.")
                else:
                    pass

        case 4:
            print("Thank you for using our app. Have a nice day!")  
            break
    print("==================================================")
    print("[1] Check Balance")
    print("[2] Withdraw Money")
    print("[3] Deposit Money")
    print("[4] Exit Application")

    print("==================================================")