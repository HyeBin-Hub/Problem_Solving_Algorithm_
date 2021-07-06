n,m=map(int,input().split())
apt=[list(input().rstrip()) for _ in range(5*n+1)]
window=[0]*5
blind=0
for col in range(1,5*m+1,5):
    for row in range(1,5*n+1):
        if apt[row][col]=="*":
            blind+=1
            if blind==4:
                window[blind]+=1
                blind=0
        elif apt[row][col]==".":
            if apt[row-1][col]=="*":
                window[blind]+=1
                blind=0
            elif apt[row-1][col]=="#":

                window[0]+=1
                blind=0
        else:
            blind=0

print(" ".join(map(str,window)))
   





                

        

            

        