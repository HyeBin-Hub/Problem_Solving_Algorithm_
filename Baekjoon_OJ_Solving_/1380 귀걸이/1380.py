count=0
while 1:
    n=int(input()) # 학생의 수
    if n==0:
        break
    name=[]
    for _ in range(n):
        name.append(input().rstrip())

    dic={}
    for _ in range(n*2-1):
        number=input().rstrip().split()
        if int(number[0]) in dic.keys():
            dic.pop(int(number[0]))
        else:
            dic[int(number[0])]=number[-1]
    count+=1
    print("{} {}".format(count,name[list(dic)[0]-1]))
            
     




    

            