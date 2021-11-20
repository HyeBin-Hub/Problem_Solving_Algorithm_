import sys
input=sys.stdin.readline

s=input()
while 1:
    a=s.replace("()","")
    if a==s:
        break
    s=a
print(len(s))