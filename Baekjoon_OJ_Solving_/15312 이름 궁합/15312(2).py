alp=[3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
a=input().rstrip()
b=input().rstrip()

save=[]

for ind,i in enumerate(a):
    save.append(alp[ord(i)-65])
    save.append(alp[ord(b[ind])-65])

while len(save)!=2:
    arr=[]
    for i in range(len(save)-1):
        arr.append((save[i] + save[i+1])%10)
    save=arr
print(*save,sep="")

