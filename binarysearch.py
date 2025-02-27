l=[-1,0,3,5,9,12]
target=9
n=len(l)#6
low=0
high=n-1 
while(low<=high):
    mid=(low+high)//2
    if(l[mid]==target):
        print(mid)
    elif(l[mid]<target):
        low=mid+1
    else:
        high=mid-1
print(-1)
        


        