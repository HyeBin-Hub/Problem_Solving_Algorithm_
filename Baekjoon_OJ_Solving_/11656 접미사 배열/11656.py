import sys
input=sys.stdin.readline
s=list(input().rstrip())
arr=[]
for i in range(len(s)):
    arr.append(s[i:])
arr.sort()
""" for i in arr:
    print("".join(i))  """
print("\n".join("".join(i) for i in arr))
