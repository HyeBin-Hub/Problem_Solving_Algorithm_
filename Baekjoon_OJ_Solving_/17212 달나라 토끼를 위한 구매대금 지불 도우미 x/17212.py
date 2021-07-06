import sys
n=int(input())

cnt=0
while 1:
    if n%7==0:
        print(cnt+n//7)
        
    if n%5==0:
        print(cnt+n//5)
   
    if n%2==0:
        print(cnt+n//2)
      
    if n==1:
        print(1)
    
