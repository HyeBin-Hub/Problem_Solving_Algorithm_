while 1:
    s=input().rstrip()
    if s=="end":
        break
    flag1=0
    flag2=1
    flag3=1

   # 1 번 조건
    for vowel in "aeiou":
        if vowel in s:
            flag1=1 
            break

    #2번 조건 
    consonant_cnt=0
    vowel_cnt=0

    for word in s:
        if word in "aeiou":
            if consonant_cnt:
                consonant_cnt=0
                vowel_cnt=1
            else:
                vowel_cnt+=1
                if vowel_cnt==3:
                    flag2=0
                    break
        else:
            if vowel_cnt:
                vowel_cnt=0
                consonant_cnt=1
            else:
                consonant_cnt+=1
                if consonant_cnt==3:
                    flag2=0
                    break
    
    # 3번 조건
    for alphabet in "abcdfghijklmnpqrstuvwxyz":
        if alphabet*2 in s:
            flag3=0
            break

    print("<"+s+"> is",end=" ")
    if flag1 and flag2 and flag3:
        print("acceptable.")
    else:
        print("not acceptable.")