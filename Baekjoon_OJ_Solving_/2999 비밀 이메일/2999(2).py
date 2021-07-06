from itertools import combinations_with_replacement
import sys
input=sys.stdin.readline
s=input().rstrip()
if len(s)>1:
    res=list(combinations_with_replacement(range(1,len(s)+1),2))
    arr=[]
    for i in res:
        if i[0]*i[1]==len(s):
            arr.append(i)

    a=max(arr)

    strs=""
    for row in range(a[0]):
        for col in range(0,len(s),a[0]):

            strs+=s[row+col]
    print(strs)
else:
    print(s)
