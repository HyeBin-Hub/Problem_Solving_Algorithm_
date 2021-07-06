import sys
n=input().rstrip()

n=list(map(int,n))
diff=[]
if len(n)==1:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
    sys.exit()
for i in range(len(n)-1):
    diff.append(n[i]-n[i+1])

if len(set(diff))==1:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    print("흥칫뿡!! <(￣ ﹌ ￣)>")



