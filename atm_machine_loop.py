pin = int(input("Enter your pin code: "))
code = 112233445566
balance = 5000

if pin == code:
    while True:
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Exit")

        option = int(input("Enter option: "))

        if option == 1:
            print("Your balance is", balance, "PKR")

        elif option == 2:
            amount = int(input("Enter your amount: "))

            if amount > balance:
                print("Insufficient balance")
            else:
                balance = balance - amount
                print("Withdraw Successful")
                print("Remaining balance is", balance, "PKR")

        elif option == 3:
            print("Exit")
            break

        else:
            print("Invalid option")

else:
    print("Wrong PIN, access denied")
