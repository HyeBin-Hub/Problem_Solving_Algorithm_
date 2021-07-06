n=int(input())
for i in range(n):
    a=int(input())
    arr=[[0]*a for i in range(a)]
    for j in range(a):
        for k in range(a):
            arr[j][k]="#"
        for q in range(1,a-1):
            for p in range(1,a-1):
                arr[q][p]="J"      
    for j in range(a):
        for k in range(a):
            print(arr[j][k],end="")
        print()
    print()