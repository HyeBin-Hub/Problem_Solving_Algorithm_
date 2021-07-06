
a,b=list(map(float,input().split()))
while 1 :
    if a==b:
        print("{:.2f}".format(a))
        break
    print("{:.2f}".format(a),end=" ")
    a=round(a+0.01,2)
