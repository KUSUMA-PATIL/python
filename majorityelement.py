l=[3,2,3]
d=dict()
for i in range(len(l)):
    if(l[i] in d):
        d[l[i]]+=1
    else:
        d[l[i]]=1
print(d)