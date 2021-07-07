# def solution(n):
#     res=""
#     while 1:
#         if n//3==1:
#             res+=str(n%3)
#             res+="1"
#             break
#         elif n//3==0:
#             res=str(n)
#             break
#         res+=str(n%3)
#         n=n//3
#     total=0
#     for ind,i in enumerate(res[::-1]):
#         total+=int(i)*(3**ind)

#     return total        


# print(solution(45))

arr=[17,14,13,12,10,17,9,8,5,8,9,12,13,15,18]
total=0
for i in arr:
    total+=i*i/sum(arr)
print(total)

print(sum(arr)/len(arr))
print(2**0)