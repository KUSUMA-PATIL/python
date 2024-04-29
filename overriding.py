
class gf:
    def fun(self):
        print("hello")
class f(gf):
    def fun(self):
        print("hey")
    def mr(self):
    
        super().fun()
pavan=f()
pavan.mr()                   
