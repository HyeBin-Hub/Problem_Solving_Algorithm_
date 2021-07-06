n=int(input())
s=input().rstrip()
a=s.replace("LL","L")
if "LL" not in s:
    print(len(s))
else:
    print(len(a)+1)