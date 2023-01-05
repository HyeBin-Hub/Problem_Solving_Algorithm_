# 버튼 A, B, C에 지정된 시간은 각각 5분, 1분, 10초이다.
# 냉동음식마다 전자레인지로 요리해야할 시간 T가 초단위로 표시되어 있다.
# 단 버튼 A, B, C를 누른 횟수의 합은 항상 최소가 되어야 한다. 

import sys

T = int(sys.stdin.readline())

buttens = [300, 60, 10]
buttens_count = [0,0,0]

# 최소 버튼 조작

for ind,butten in enumerate(buttens):
    if T >= butten:
        # print(butten)
        count = T // butten 
        # print(count)
        T -= butten * count 
        # print(T)
        buttens_count[ind] = count

if T != 0:
    print(-1) 
else:
    print(*buttens_count) 



