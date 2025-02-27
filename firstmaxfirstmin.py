n=int(input("Enter N value:"))
a=[int(input()) for _ in range(n)]
a.sort()
for i in range(n//2):
     print(a[n-i-1]," ",(a[i]))
     
if n%2!=0:
     print(a[n//2])
        

        