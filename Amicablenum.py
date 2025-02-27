x=int(input("enter value of x:"))
y=int(input("enter value of y:"))
sum1=0
sum2=0
for i in range(1,x):
    if(x%i==0):
        sum1=sum1+i
        
for i in range(1,y):
    if(y%i==0):
        sum2=sum2+i
print("Factor of x",sum1)
print("Factor of y",sum2)
if(sum1==y and sum2==x):
    print("Amicable pair numbers")
else:
    print("not an Amicable pair numbers")