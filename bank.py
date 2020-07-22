#class methods 
#Michelle  Nthumo
class BankAccount:
  bank="KCB"
  
  def __init__(self,first_name,last_name,phone_number):
    self.first_name=first_name
    self.last_name=last_name
    self.phone_number=phone_number
    self.balance=0
    
    
  def account_name(self):
    name="{} account for {} {}".format(self.first_name,self.last_name, self.phone_number)
    return  name
    

  def deposit(self,amount):
    self .balance+=amount
    if amount>0:
      print("You have deposited {} to your account". format(amount))
    else:
      print("The deposit of {} cannot be offered ".format(amount))
    
  def deposit_statement(self):
    statement="deposit statement for".format(self.first_name)
  
    def get_balance(self):
      print("The balance for {} is {} ".format(self.account_name(),self.balance))
  
  def withdraw(self,amount):
    amount>0
    if self.balance>=amount:
      self.balance-=amount
      print("You have withdrawn {} from your account".format(amount))
    elif amount > self.balance:
      print("You have insufficient balance to withdraw {}".format(amount))  
def loan_repay(self,amount):
    if amount>=1:
        self.repay=self.loans-amount
        print("your loan has been repayed")

acc2=BankAccount("Michelle", +254720604378, "Nthumo")
acc1=BankAccount("Charl", +254789568467, "Olivia")
acc2.deposit(10)
acc1.deposit(700)
acc2.deposit(500)
acc1.deposit(-60)
acc1.deposit(20)

acc1.withdraw(150)
acc2.withdraw(45)
acc2.withdraw(600)
acc1.withdraw(750)


print(acc2.get_balance())
print(acc1.get_balance())
print(acc1.deposit())