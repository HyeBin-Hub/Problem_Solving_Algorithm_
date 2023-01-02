s = list(map(int,input().rstrip().split()))

if s == sorted(s):
    print("ascending")
elif s == sorted(s,reverse=True):
    print("descending")
else:
    print("mixed")
