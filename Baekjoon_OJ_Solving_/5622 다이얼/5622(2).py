dic={2:["A","B","C"],3:["D","E","F"],
     4:["G","H","I"],5:["J","K","L"],
     6:["M","N","O"],7:["P","Q","R","S"],
     8:["T","U","V"],9:["W","X","Y","Z"]}
n=input()
arr=[]
for k,v in dic.items():
    for i in v:
        for j in n:
            if j in i:
                arr.append(k+1)

print(sum(arr))