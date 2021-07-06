n,m=map(int,input().split())# 박스의 개수, 책의 개수
box=list(map(int,input().split()))# 박스 용량
book=list(map(int,input().split()))# 책의 크기

print(sum(box)-sum(book))
