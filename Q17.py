class Bank_Account: 
    def make_account(self): 
        self.balance=0
        print("Deposit & Withdrawal") 
  
    def deposit(self): 
        amount = float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print("Amount Deposited:",amount) 
  
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance >= amount: 
            self.balance -= amount 
            print("Amount Withdrawn:", amount) 
        else: 
            print("Insufficient balance  ") 
  
    def display(self): 
        print("Net Available Balance=",self.balance) 

Acc = Bank_Account()
Acc.make_account()
Acc.deposit() 
Acc.withdraw() 
Acc.display()
