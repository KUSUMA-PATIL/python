class SBI:
    branch_code=7056
    maintainance_amt=100
    
    def __init__(self,name,mob_no,age):
        self.Acc_holder_name=name
        self.Mob_no=mob_no
        self.age=age
        self.balance=0
        
    def deposit(self, amt):
        self.balance = self.balance + amt
        
    def withdraw(self,amt):
            if(self.balance>=amt):
                self.balance=self.balance - amt
                return"sufficient balance"
            else:
                print("insuffienct balance")
                    
    def transfer(self,sender_acc,amt):
            transfer_cond=sender_acc.withdraw(amt)
            if(transfer_cond =="sufficient balance"):
                self.deposit(amt)
            
    def print_balance(self):
         print(self.balance)
    @classmethod  
    def maintainance_charges(cls,list_acc): 
        for every_acc in list_acc:
            every_acc.balance=every_acc.balance-cls.maintainance_amt
    @staticmethod
    def thank_you():
        print("thank you")
         
chotu_acc=SBI("chotu","8296875008","20")
BITM_acc=SBI("BITM","9980839092","23")
chotu_acc.deposit(500000)
BITM_acc.deposit(100000)
print(chotu_acc.balance)
print(BITM_acc.balance)
chotu_acc.withdraw(25000)
print(chotu_acc.balance)
chotu_acc.transfer(BITM_acc,25000)
print(chotu_acc.balance)
chotu_acc.print_balance()
list_acc=[chotu_acc,BITM_acc]
SBI.maintainance_charges(list_acc)

chotu_acc.print_balance()
BITM_acc.print_balance()









      
    
        