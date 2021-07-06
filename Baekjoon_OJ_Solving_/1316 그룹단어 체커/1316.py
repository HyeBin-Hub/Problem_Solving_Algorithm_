n=int(input())
count=0
flag=0
for _ in range(n):
    s=input().rstrip()
    stack=[]
    for i in range(len(s)):
        stack.append(s[i])
        if s[i] in stack[:i-1]:
            if s[i]==stack[i-1]:
                flag=1
            else:
                flag=0
                break
        else:
            flag=1
    if flag:
        count+=1

print(count)