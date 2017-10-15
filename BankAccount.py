class Account():
    def __init__(self):
        self.__balance=0

    def getbalance (self):
        return float(self.__balance)

    def setbalance(self,amt):
        self.__balance=amt
        return self.__balance

    def deposit(self,amt):
        self.__balance=int(self.__balance)+amt
        return float(self.__balance)

    def withdraw(self,amt):
        self.__balance=float(self.__balance)-amt
        return float(self.__balance)