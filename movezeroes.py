l=[0,1,0,3,12]
d=[]
c=0
for i in range (len(l)):
    if(l[i]!=0):
        d.append(l[i])
    else:
        c+=1
for i in range(c):
    d.append(0)
print(d)