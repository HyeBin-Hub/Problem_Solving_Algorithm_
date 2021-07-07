def solution(n, arr1, arr2):

    answer=[[" "]*n for _ in range(n)]
    
    for ind,i in enumerate(arr1):
        a=list(format(i,"b").zfill(n))
        for ind2,j in enumerate(a):
            if j=="1":
                answer[ind][ind2]="#"
            
    for ind,i in enumerate(arr2):
        a=list(format(i,"b").zfill(n))
        for ind2,j in enumerate(a):
            if j=="1":
                answer[ind][ind2]="#"

    for ind, i in enumerate(answer):
        answer[ind]="".join(i)

    return answer