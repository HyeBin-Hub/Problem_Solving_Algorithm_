s=input()
arr=[s.count(str(i)) for i in range(10)]
arr[6]=(arr[6]+arr[9]+1)//2
arr[9]=arr[6]
print(max(arr))