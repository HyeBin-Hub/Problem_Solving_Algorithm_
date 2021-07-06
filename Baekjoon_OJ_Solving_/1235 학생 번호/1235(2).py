

n=int(input())
student_number=[input().rstrip() for _ in range(n)]
student_number_len=len(student_number[0])


for i in range(1,student_number_len+1):
    res=[]

    for j in student_number:
        res.append(j[-i:])

    if len(set(res))==len(res):
        print(i)
        break





# arr=[1,2,3,4,5,6,7,8,9]
# print(arr[-1:])
# print(arr[-2:])
# print(arr[-3:])   
# print(arr[-4:])
# print(arr[-5:])
# print(arr[-6:])
# print(arr[-7:])
# print(arr[-8:])
# print(arr[-9:])
