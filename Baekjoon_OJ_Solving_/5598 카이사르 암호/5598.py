import sys
input=sys.stdin.readline
s=input().rstrip()
for i in s:
    if "D"<=i <="Z":
        print(chr(ord(i)-3),end="")
    else:
        print(chr(ord(i)+23),end="")