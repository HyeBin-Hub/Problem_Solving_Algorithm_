from collections import deque
deq=deque([])
while 1:
    s=input().rstrip()
    if s=="고무오리 디버깅 끝":
        break
    if s=="고무오리 디버깅 시작":
        continue
    if s=="문제":
        deq.append(s)
    else:
        if not deq:
            deq.appendleft("문제")
            deq.appendleft("문제")
        else:
            deq.pop()
if not deq:
    print("고무오리야 사랑해")
else:
    print("힝구") 