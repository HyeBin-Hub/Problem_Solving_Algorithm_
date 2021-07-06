
import sys
input=sys.stdin.readline
n=int(input())
arr=[int(input()) for _ in range(n)]

print(round(sum(arr)/n))

arr.sort()
print(arr[n//2])


from collections import Counter
dic=Counter(arr)
dics=dic.most_common()

if len(arr)>1:
    if dics[0][1]==dics[1][1]:
        print(dics[1][0])
    else:
        print(dics[0][0])
else:
    print(dics[0][0])
    

print(max(arr)-min(arr))
