# Creating the class "Budget"
class Budget:
    # Calling the method
    def __init__(self, Food=500, Clothing=700, entertainment=0):
        
        # Creating the class variables as Category
        self.Food = Food
        self.Clothing = Clothing
        self.entertainment = entertainment

    # Creating the Instance Methods
    def deposit(self):
        print("================================")
        print("Welcome to Deposit! Choose a category?")
        print("================================")

        # Check to ensure user input is an integer
        while True:
            try:
                deposit_input = int(input("Select Deposit Category?\n"
                                          "(1). Food \n"
                                          "(2). Clothing \n"
                                          "(3). Entertainment \n"
                                          ))
                break
            except ValueError:
                print("Invalid selection please try again! \n")

        if deposit_input == 1:
            print("Food Category")
            while True:
                try:
                    deposit_amount_input = int(input("How much would you like to deposit? \n"))
                    break
                except ValueError:
                    print("Invalid Selection, Please try again!... \n")

            self.Food += deposit_amount_input
            print("================================")
            print(f"#{deposit_amount_input} has been deposited in the Food category")
            print("================================")
        elif deposit_input == 2:
            print("Clothing Category")
            while True:
                try:
                    deposit_amount_input = int(
                        input("How much would you like to deposit? \n"))
                    break
                except ValueError:
                    print("Invalid Selection, Please try again!... \n")

            self.Clothing += deposit_amount_input
            print("================================")
            print(f"#{deposit_amount_input} has been deposited in the Clothing category")
            print("================================")

        elif deposit_input == 3:
            print("Entertainment Category")
            while True:
                try:
                    deposit_amount_input = int(
                        input("How much will you like to deposit? \n"))
                    break
                except ValueError:
                    print("Invalid Selection, Please try again!... \n")

            self.entertainment += deposit_amount_input
            print("================================")
            print(f"#{deposit_amount_input} has been deposited in the Entertainment category")
            print("================================")
        else:
          print("Invalid category, try again")



    def withdraw(self):
        print("================================")
        print("Welcome to Withdrawals")
        print("================================")

        while True:
            try:
                withdrawal_input = int(input("Select Withdrawal Category?\n"
                                             "(1). Food \n"
                                             "(2). Clothing \n"
                                             "(3). Entertainment \n"
                                             ))
                break
            except ValueError:
                print("Invalid category, try again! \n")

        if withdrawal_input == 1:
            print("Food Category")
            while True:
                try:
                    withdrawal_amount_input = int(
                        input("How much will you like to withdraw? \n"))
                    break
                except ValueError:
                    print("Invalid category, try again! \n")

            self.Food -= withdrawal_amount_input
            print("================================")
            print(f"#{withdrawal_amount_input} has been withdrawn from Food Category")
            print("================================")

        elif withdrawal_input == 2:
            print("Clothing")
            while True:
                try:
                    withdrawal_amount_input = int(
                        input("How much will you like to withdraw? \n"))
                    break
                except ValueError:
                    print("Invalid category, try again! \n")

            self.Clothing -= withdrawal_amount_input
            print("================================")
            print(f"#{withdrawal_amount_input} has been withdrawn from Clothing Category")
            print("================================")

        elif withdrawal_input == 3:
            print("Entertainment")
            while True:
                try:
                    withdrawal_amount_input = int(
                        input("How much will you like to withdraw? \n"))
                    break
                except ValueError:
                    print("Invalid category, try again! \n")

            self.entertainment -= withdrawal_amount_input
            print("================================")
            print(f"#{withdrawal_amount_input} has been withdrawn from Entertainment Category")
            print("================================")
        else:
            print("Invalid category, try again! \n")

    def transfer(self):
        while True:
            try:
                transfer_input = int(input("Choose account to debit from?\n"
                                           "(1). Food \n"
                                           "(2). Clothing \n"
                                           "(3). Entertainment \n"
                                           ))

                break
            except ValueError:
                print("Invalid category, try again! \n")

        print("Balance in category: \n")
        budget.check_balance()
        print("================================")

        while True:
            try:
                input_transfer = int(input("Choose destination Category?\n"
                                           "(1). Food \n"
                                           "(2). Clothing \n"
                                           "(3). Entertainment \n"
                                           ))
                break
            except ValueError:
                print("Invalid category, try again! \n")

        while True:
            try:
                transfer_amount = int(input("How much will you like to transfer: \n"))
                break
            except ValueError:
                print("Invalid category, try again! \n")

        if transfer_input == 1 and input_transfer == 2:
            self.Clothing += transfer_amount
            self.Food -= transfer_amount
            print(f"#{transfer_amount} has been transferred from Food to Clothing Category")
        elif transfer_input == 1 and input_transfer == 3:
            self.entertainment += transfer_amount
            self.Food -= transfer_amount
            print(f"#{transfer_amount} has been transferred from Food to Entertainment Category")
        elif transfer_input == 2 and input_transfer == 1:
            self.Food += transfer_amount
            self.Clothing -= transfer_amount
            print(f"#{transfer_amount} has been transferred from Clothing tO Food Category")
        elif transfer_input == 2 and input_transfer == 3:
            self.entertainment += transfer_amount
            self.Clothing -= transfer_amount
            print(f"#{transfer_amount} has been transferred from Clothing TO Entertainment Category")
        elif transfer_input == 3 and input_transfer == 1:
            self.Food += transfer_amount
            self.entertainment -= transfer_amount
            print(f"#{transfer_amount} has been transferred from Entertainment to Food Category")
        elif transfer_input == 3 and input_transfer == 2:
            self.Clothing += transfer_amount
            self.entertainment -= transfer_amount
            print(f"#{transfer_amount} has been transferred from Entertainment tO Clothing Category")
        else:
            print("Invalid Transfer! \n Cannot Transfer into the same Category \n")

    def check_balance(self):
        print(f"Current balance:\n"
              f"(1). Food = #{self.Food} \n"
              f"(2). Clothing = #{self.Clothing} \n"
              f"(2). Entertainment = #{self.entertainment} \n \n"
              f" TOTAL BALANCE : #{self.Clothing + self.Food + self.entertainment} \n"
              )

# instantiating the class
budget = Budget()

task_force = True
# A loop to run the code as long as any other number is inputed by the user.
while task_force:
    while True:
        try:
            decision_input = int(input("WHAT WOULD YOU LIKE TO DO?\n"
                                       "(1). DEPOSIT \n"
                                       "(2). WITHDRAW \n"
                                       "(3). TRANSFER\n"
                                       "(4). CHECK BALANCE\n"
                                       "PRESS ANY OTHER KEY TO LOGOUT "
                                       ))
            break
        except ValueError:
            print("Invalid category, try again! \n")

    if decision_input == 1:
        budget.deposit()
        budget.check_balance()

    elif decision_input == 2:
        budget.withdraw()
        budget.check_balance()

    elif decision_input == 3:
        budget.transfer()
        budget.check_balance()

    elif decision_input == 4:
        print("================================")
        print("")
        print("================================")
        budget.check_balance()
    else:
        task_force = False