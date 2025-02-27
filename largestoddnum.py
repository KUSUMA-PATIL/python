l="52"
str=len(l)
ans=""
for i in range(len(l)):
    if(int(l[i])%2==1):
        ans=l[0:i+1]
print(ans)
        
