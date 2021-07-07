def solution(a, b):
    sum=0
    if a>b:
        a,b=b,a
    for i in range(a,b+1):
        sum+=i

    return sum

print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))