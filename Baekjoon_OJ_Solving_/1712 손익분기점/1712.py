a,b,c=map(int,input().split())
print((a+b-c)//(c-b)+2 if c>b else -1)