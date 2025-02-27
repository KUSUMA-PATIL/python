nums=[1,1,0,1,1,1]
maxi=0
c=0
for i in nums:
    if(i==0):
        c=0
    else:
        c+=1
        maxi=max(maxi,c)
print (maxi)