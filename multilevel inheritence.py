
class gf:
    def __init__(self):
        self.property=1000000
class F(gf):
    def __init__(self):
        super().__init__()
        self.father_property=5000000+self.property
        
class pavan(F):
    def __init__(self):
        super().__init__()
        self.my_property=self.father_property+100000
my_father=pavan()
print(my_father.my_property)

                
    