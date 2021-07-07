def solution(arr,commands):
    arr2=[]
    for i in commands:
        a=arr[i[0]-1:i[1]]
        a.sort()
        arr2.append(a[i[2]-1])
    return arr2