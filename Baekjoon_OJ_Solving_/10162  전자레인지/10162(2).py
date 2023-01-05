import sys

T = int(sys.stdin.readline())

if T%10:
    print(-1)
else:
    print(T//300,(T-T//300*300)//60,T%60//10)


