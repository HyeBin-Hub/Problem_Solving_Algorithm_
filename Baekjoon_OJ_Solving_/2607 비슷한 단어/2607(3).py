n=int(input())
first=list(input().rstrip())
res=0
for _ in range(n-1):
    first_Word=first[:]
    check_word=list(input().rstrip())

    for i in range(len(check_word)):
        a=check_word.pop(0)
        if a in first_Word:
            first_Word.remove(a)
        else:
            check_word.append(a)
    check_len=len(check_word)
    first_len=len(first_Word)

    if (check_len==0 and first_len==0) or (check_len==0 and first_len==1) or (check_len==1 and first_len==0) or (check_len==1 and first_len==1):
        res+=1
print(res)
