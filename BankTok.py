from BankCustomer import Customer

class Bank():
    def __init__(self,bankname):
        self.__bankname=bankname
        self.__cuslist=[]
        self.numcustomers=0

    def addcustomer(self,firstname,lastname):
        cus=Customer(firstname,lastname)
        self.fn=cus.getfirstname()
        self.fl=cus.getlastname()
        self.name=str(self.fn)+" "+str(self.fl)
        self.__cuslist.append(self.name)
        return self.__cuslist

    def getnumcustomers(self):
        self.numcustomers=len(self.__cuslist)
        return self.numcustomers

    def getcustomers(self):
        return self.__cuslist

    def custoption(self):
        cus=Customer(self.fn,self.fl)
        while True:
            op=int(input("\nWelcome to Your Customer Menu\n"
                        "1.Get First Name\n"
                        "2.Get Last Name\n"
                        "3.Go to Bank Account Menu\n"
                        "To Do     : "))
            if op==1:
                print(cus.getfirstname())
            elif op==2:
                print(cus.getlastname())
            elif op==3:
                cus.accoption()
            else:
                break