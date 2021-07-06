import sys
input=sys.stdin.readline
n,b=input().rstrip().split()
b=int(b)
count=0
for ind,val in enumerate(n[::-1]):
    if "A"<=val<="Z":
        count+=(ord(val)-55)*(b**ind)
    else:
        count+=int(val)*(b**ind)
print(count)