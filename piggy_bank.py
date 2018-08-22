import sys


class Account:
    def __init__(self):
        # set account balance to 0.
        # call loop function to interact with user
        self.balance = 0
        print('---------------------Start---------------------')
        self.loop()

    # function to add balance to the account
    def add(self):
        # type case input to float
        amount = float(input('add amount: '))
        self.balance += amount
        print(f'After adding, your updated balance is {self.balance} rupees \n')

    # function to check balance of the account
    def check(self):
        print(f'Your current balance is {self.balance} rupees \n')

    # function to withdraw balance from the account
    def withdraw(self):
        # type case input to float
        amount = float(input('Withdraw amount: '))
        if amount <= self.balance:
            self.balance -= amount
            print(f'After withdrawing, balance amount is {self.balance} rupees \n')
        else:
            print(f'Not enough balance. Your balance is {self.balance} \n')

    def loop(self):
        # define a dict to map input with function name
        functions = {'add': self.add, 'check': self.check, 'withdraw': self.withdraw}
        run = (input('Start or End: ')).lower()
        if run != 'start':
            print(f'Bye! have a nice day \n')
            # return f'Bye! have a nice day'
            sys.exit()
        # keep on executing loop until user input is not start
        while run == 'start':
            # get function name as input
            fn = (input('Add, Withdraw or Check: ')).lower()
            # check input is correct or not. If not ask user to input correct function.
            if fn in functions.keys():
                functions[fn]()
                run = (input('Start or End: ')).lower()
                if run != 'start':
                    print(f'Bye! have a nice day \n')
            else:
                print('please enter correct operation \n')

# account = Account()
# print(account.check())
