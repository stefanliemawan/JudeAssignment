from BankAccount import Account

class Customer():

    def __init__(self,firstname,lastname):
        self.__firstname=firstname
        self.__lastname=lastname

    def getfirstname(self):
        return self.__firstname

    def getlastname(self):
        return self.__lastname

    def accoption(self):
        acc=Account()
        while True:
            op=int(input("\nWelcome to Your Bank Account Menu\n"
                    "1.Get Balance\n"
                    "2.Set Balance\n"
                    "3.Deposit\n"
                    "4.Withdraw\n"
                    "To Do   :"))
            if op==1:
                print(acc.getbalance())
            elif op==2:
                acc.setbalance(int(input("Set Balance   : ")))
            elif op==3:
                acc.deposit(int(input("Deposit    : ")))
            elif op==4:
                acc.withdraw(int(input("Withdraw  : ")))
            else:
                break