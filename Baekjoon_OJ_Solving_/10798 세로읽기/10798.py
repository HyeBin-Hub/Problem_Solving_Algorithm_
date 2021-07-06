arr=[input()for i in range(5)]
arr2=[len(i)for i in arr]
for i in range(max(arr2)):
    for j in range(5):
        if i>=arr2[j]:
            continue
        else:
            print(arr[j][i],end="")