def solution(a, b):
    res=0
    for i in range(len(a)):
        res+=a[i]*b[i]
    return res

print(solution([1,2,3,4],[-3,-1,0,2]))