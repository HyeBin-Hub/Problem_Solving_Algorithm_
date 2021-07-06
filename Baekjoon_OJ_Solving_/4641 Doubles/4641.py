while 1:
    s=list(map(int,input().split()))
    if s==[-1]:
        break
    count=0
    for i in range(len(s[:-1])):
        if s[i]*2 in s:
            count+=1
    print(count)
