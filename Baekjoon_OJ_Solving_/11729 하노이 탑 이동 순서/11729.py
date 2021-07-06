def run(n,a,b,c):
    if n==1:
        move.append([a,c])
    else:
        run(n-1,a,c,b)
        move.append([a,c])
        run(n-1,b,a,c)
move=[]
n=int(input())
run(n,1,2,3)

print(len(move))
for row in move:
    for i in row:
        print(i,end=" ")
    print()
        #print(" ".join(str(i)))
    