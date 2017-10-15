from BankTok import Bank

def main():
    bank=Bank(str(input("Type Your Bank Name  : ")))
    while True:
        op=int(input("\nWelcome to your Bank Menu\n"
                    "1.Add Customer\n"
                    "2.Get Customers Number\n"
                    "3.Get Customers\n"
                    "4.Go to Your Customer Menu\n"
                    "To Do     : "))
        if op==1:
            bank.addcustomer(str(input("First Name  : ")),str(input("Last Name  : ")))
        elif op==2:
            print(bank.getnumcustomers())
        elif op==3:
            print(bank.getcustomers())
        elif op==4:
            bank.custoption()
        else:
            break

main()