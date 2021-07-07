from itertools import combinations
def solution(numbers):
    res=set()
    arr=list(combinations(numbers,2))
    for i in arr:
        res.add(sum(i))
    return sorted(list(res))
print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))