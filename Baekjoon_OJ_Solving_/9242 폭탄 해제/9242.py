num={0:[['***', '* *', '* *', '* *', '***']], 1:[['  *', '  *', '  *', '  *', '  *']], 2:[['***', '  *', '***', '*  ', '***'],['***', '  *', '***', '*', '***']], 3:[['***', '  *', '***', '  *', '***']], 4:[['* *', '* *', '***', '  *', '  *']], 5:[['***', '*  ', '***', '  *', '***'],['***', '*', '***', '  *', '***']], 6:[['***', '*  ', '***', '* *', '***'],['***', '*', '***', '* *', '***']], 7:[['***', '  *', '  *', '  *', '  *']], 8:[['***', '* *', '***', '* *', '***']], 9:[['***', '* *', '***', '  *', '***']]}

import sys
input=sys.stdin.readline
res=[i.rstrip() for i in sys.stdin]

total=""
for start_col in range(0,len(res[0]),4):
    arr=[]
    for row in range(5):
        arr.append(res[row][start_col:start_col+3])
    
    for k,v in num.items():
        if k==2 or k==5 or k==6:
            if arr==v[0]  :
                total+=str(k)
            elif arr==v[1]:
                total+=str(k)

        else:
            if  arr==v[0]:
                total+=str(k)
                
if int(total)%6==0:
    print("BEER!!")
else:
    print("BOOM!!")