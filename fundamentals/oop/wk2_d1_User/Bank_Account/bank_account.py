class BankAccount:
    # don't forget to add some default values for these parameters!
    accounts = []
    def __init__(self, int_rate, balance): 
        #Create a Bank Account class with the attributes interest rate abnd balance
        self.int_rate = int_rate
        self.balance = balance
        # don't worry about user info here; we'll involve the User class soon
        #BankAccount.accounts.append(self)


    def deposit(self, amount):
        #Add a deposit method to the BankAccount class
        self.balance += amount
        return(self)



    def withdraw(self, amount):
        # Add a withdraw method to BankAccount class
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print('Insuffiecient Funds: Charging $5')
            self.balance -= 5
        return(self)



    def display_account_info(self):
        # add a display_account_info method to Bank account class
        print(f'Your account balance is: {self.balance}')
        return(self)


    def yield_interest(self):
        #Adding a yield_interest method to BankAccounts class as long as the account is positive
        if self.balance > 0:
            self.balance =  self.balance + (self.balance * self.int_rate)
        return(self)

    #Not sure why this isn't working.... "Check in Discord to see if anyone has a solution"
    #@classmethod
    #def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info(self)





account_1 = BankAccount(.015, 3750)
account_2 = BankAccount(.02, 5000)


account_1.deposit(20).deposit(50).deposit(500).withdraw(130).yield_interest().display_account_info()
#trying a way of displaying i found online with \ not sure which one i like better
account_2.deposit(100)\
        .deposit(300)\
            .withdraw(50)\
                .withdraw(420)\
                    .withdraw(25).\
                        withdraw(200).\
                            yield_interest()\
                                .display_account_info()