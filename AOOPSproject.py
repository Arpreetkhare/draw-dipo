class Account:
    def __init__(self,act1,ballence):
        self.act1=act1
        self.ballence=ballence
        
        
    def deposit(self,depomoney): 
        self.depomoney=depomoney
        currentball=  self.ballence + self.depomoney
        return f'curreent ballence is {currentball}rs'
    
    
    def withdrawals(self,withdrawnmoney):
        self.withdrawnmoney=withdrawnmoney
        avball=self.ballence - self.withdrawnmoney
        if self.withdrawnmoney<= self.ballence:
         return f'available bllence is {avball}rs'
        else:
         return 'you dunno have that much money'

         
        
cheack=Account('jose',200)
print(cheack.ballence)
print(cheack.act1)
print(cheack.withdrawals(1000))
print(cheack.deposit(300))
          