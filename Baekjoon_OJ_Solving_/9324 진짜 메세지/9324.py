import sys
input=sys.stdin.readline
def run():
    n=int(input())
    for i in range(n):
        s=input().rstrip()+"0"
        d={}
        flag=0
        for ind,j in enumerate(s):
            d[j]=d.get(j,0)+1
            if d[j]>=3:
                r=s[ind+1]
                # FAKE의 경우
                if s[ind+1]=="0" or j!=s[ind+1]:
                    flag=1
                    break
                else:
                    d[j]=-1
                
        if flag:
            print("FAKE")
        else:
            print("OK")
run()
