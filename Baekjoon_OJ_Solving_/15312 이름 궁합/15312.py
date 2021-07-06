import sys
input=sys.stdin.readline
alp={"A":3, "B":2, "C":1, "D":2, "E":3, "F":3, "G":2, "H":3, "I":3, "J":2, "K":2, "L":1, "M":2, "N":2, "O":1, "P":2, "Q":2, "R":2, "S":1, "T":2, "U":1, "V":1, "W":1, "X":2, "Y":2, "Z":1}
A=input().rstrip()
B=input().rstrip()
res=""
for i in range(len(A)):
    res+=A[i]+B[i]

r=[alp[res[i]]+alp[res[i+1]] for i in range(len(res)-1)]
while 1:
    a=[]
    for i in range(len(r)-1):
        b=str(r[i]+r[i+1])
        if int(b)<10:
            a.append(int(b))
        else:
            a.append(int(b[1]))
   
    if len(a)==2:
        print("".join(map(str,a)))
        break
    r=a
