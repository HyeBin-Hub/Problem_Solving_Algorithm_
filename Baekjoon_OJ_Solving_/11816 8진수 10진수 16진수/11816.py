import sys
input=sys.stdin.readline
n=input().rstrip()
if n[0]=="0":
    if n[1]=="x":#(16진수)
        print(int(n,16))
    else:

        print(int(n[0]+"o"+n[0:],8))
else:
    print(n)
