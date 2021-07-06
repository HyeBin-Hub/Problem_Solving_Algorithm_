from bisect import bisect_left,bisect_right
n=int(input())
arr=[60,70,80,90]
val=["F","D","C","B","A"]
print(val[bisect_right(arr,n)])