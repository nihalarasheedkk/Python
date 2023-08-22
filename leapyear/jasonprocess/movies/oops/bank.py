class Bank:

    accountnum:int
    balance:int
    ac_type:str
    pe_name:str

    def create_account(self,accountno,bal,ac_type,name):

        self.accountnum=accountno
        self.balance=bal
        self.ac_type=ac_type
        self.pe_name=name

    def deposit(self,amount):
        self.balance+=amount
        print(f"ur sbk account {self.accountnum} has been credited with amount{amount}aval bal is {self.balance}")

    def withdraw(self,amount):

        if self.balance>=amount:
            self.balance-=amount
            print(f"ur sbk ac {self.accountnum} has been debited with amt {amount} aval bal is {self.balance}")
        else:
            print("transactn failed insufficient bal")

obj1=Bank()
obj1.create_account(100,2000,"savings","hari")
obj1.withdraw(1000)            
    
       

        


