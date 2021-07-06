n=input()
a=int(n[1]+n[0])*2
if a>99:
    a=a%100
    
if a<=50:
    print(a)
    print("GOOD")
else:
    print(a)
    print("OH MY GOD")

