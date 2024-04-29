
class gf:
    def __init__(self,surname):
        self.surname=surname
class father(gf):
    def __init__(self,name,surname):
        self.name=name
        super().__init__(surname)
                
my_father=father("father_name","KS") 
print(my_father.surname)                    