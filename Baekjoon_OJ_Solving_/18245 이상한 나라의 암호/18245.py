import sys
input=sys.stdin.readline
i=2
while 1:
    s=input().rstrip()
    if s=="Was it a cat I saw?":
        break
    s=list(s)
    print("".join(s[0::i]))
    i+=1