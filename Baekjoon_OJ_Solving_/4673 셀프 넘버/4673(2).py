def abc():
    arr=[0]*10001
    i=0
    while i<9:
        i+=1
        a=i+i
        arr[a]=a
    while i<99:
        i+=1
        a=i+(i//10)+(i%10)
        arr[a]=a
    while i<999:
        i+=1
        a=i+(i//100)+((i%100)//10)+((i%100)%10)
        arr[a]=a
    while i<9999:
        i+=1
        a=i+(i//1000)+((i%1000)//100)+((i%100)//10)+((i%100)%10)
        if a<9999:
            arr[a]=a
    for i in range(9999):
        if arr[i]==0 and i>0 :
            print(i)
abc()