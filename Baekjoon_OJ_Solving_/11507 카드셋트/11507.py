import sys
input=sys.stdin.readline
s=input().rstrip()
arr=""
P=K=H=T=13
for i in range(0,len(s),3):
    a=s[i:i+3]
    if a not in arr:   
        if a[0]=="P":
            P-=1
        elif a[0]=="K":
            K-=1
        elif a[0]=="H":
            H-=1
        elif a[0]=="T":
            T-=1
    else:
        print("GRESKA")
        sys.exit()
    arr+=a
print(P,K,H,T)
