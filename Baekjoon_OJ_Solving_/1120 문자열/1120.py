import sys
a,b=input().rstrip().split()
total=sys.maxsize

for i in range(len(b)-len(a)+1):
        cnt=0
        if len(b)-len(a)!=0:
            for j,k in zip(a,b[i:]):
                if j!=k:
                    cnt+=1
            total=min(total,cnt)
        else:
            for j,k in zip(a,b[i:]):
                if j!=k:
                    cnt+=1
            total=min(total,cnt)
print(total)
            




