import sys
input=sys.stdin.readline
n=input()
alp=[-1]*26
for i in range(97,123):
    for j in n:
        if chr(i) == j:
            alp[i-97]=n.index(j)
print(" ".join(map(str,alp)))