
balance = 500.00
deposit_count = 0
withdrawal_count = 0
running = True

print("Welcome to the Banking System!")
print(f"Your initial balance is R$ {balance:.2f}")

while running:
    print("\nMENU")
    print("1 - Deposit")
    print("2 - Withdraw")
    print("3 - Check balance")
    print("4 - Exit")

    try:
        option = int(input("Choose an option: "))

        if option == 1:
            try:
                deposit_amount = float(input("Enter the deposit amount: R$ "))

                if deposit_amount <= 0:
                    print("Error: The deposit amount must be positive.")
                else:
                    balance += deposit_amount
                    deposit_count += 1
                    print(f"Deposit of R$ {deposit_amount:.2f} completed successfully.")
                    print(f"Your new balance is R$ {balance:.2f}")

            except ValueError:
                print("Error: Invalid amount. Enter a number for the deposit.")

        elif option == 2:
            try:
                withdrawal_amount = float(input("Enter the withdrawal amount: R$ "))

                if withdrawal_amount <= 0:
                    print("Error: The withdrawal amount must be positive.")
                elif withdrawal_amount > balance:
                    print("Error: Insufficient balance to complete the withdrawal.")
                    print(f"Your current balance is R$ {balance:.2f}")
                else:
                    balance -= withdrawal_amount
                    withdrawal_count += 1
                    print(f"Withdrawal of R$ {withdrawal_amount:.2f} completed successfully.")
                    print(f"Your new balance is R$ {balance:.2f}")

            except ValueError:
                print("Error: Invalid amount. Enter a number for the withdrawal.")

        elif option == 3:
            print(f"Your current balance is R$ {balance:.2f}")

        elif option == 4:
            print("Closing the banking system.")
            running = False

        else:
            print("Invalid option. Choose a number between 1 and 4.")

    except ValueError:
        print("Error: Invalid input. Enter a number to choose an option.")

print(f"Number of deposits made: {deposit_count}")
print(f"Number of withdrawals made: {withdrawal_count}")
print(f"Final balance: R$ {balance:.2f}")

