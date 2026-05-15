class Bankaccount:
    def __init__(self, owner , balance = 100000 ):
        self.owner =  owner 
        self.balance = balance 
    def deposite (self,amount) :
        self.balance =  self.balance + amount
        print (f"{self.balance} balance after deposite")
    def withdraw (self,amount):
        if(amount>self.balance):
            print("Insufficient balance")
        else:    
            self.balance =  self.balance - amount
            print (f"{self.balance} balance after withdraw")
        


print ("Then name of the owner ")
name = input ()
print("money to  deposite ")
depo = int (input())
print("money to withdraw")
withd = int(input())

bank = Bankaccount(name)
bank.deposite(depo)
bank.withdraw(withd)