
s=input().rstrip()
arr=[[":fan:"]*3 for _ in range(3)]
arr[1][1]=":{}:".format(s)
for i in arr:
    print("".join(i))