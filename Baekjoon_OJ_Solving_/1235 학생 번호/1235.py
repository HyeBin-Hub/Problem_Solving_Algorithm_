n=int(input())
student_number=[input().rstrip() for _ in range(n)]
student_number_len=len(student_number[0])

count=0
for i in range(1,student_number_len+1):
    res=[]
    flag=0
    for j in student_number:
        res.append(j[-i:])
    for j in range(n-1):
        for k in range(j+1,n):
            if res[j]==res[k]:
                flag=1 # 안되는거
                break

    if flag==0:
        print(len(res[0]))
        break
    else:
        continue