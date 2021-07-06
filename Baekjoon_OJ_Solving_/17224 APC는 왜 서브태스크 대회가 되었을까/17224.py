# from itertools import combinations
# n,l,k=map(int,input().split())

# res=list(combinations(range(n),k))

# sub=[list(map(int,input().split())) for _ in range(n)]

# mins=0

# for i in res:
#     total=0
#     for j in i:
#         if sub[j][1] <= l:
#             total+=140
#         else: # sub[j][1] > l
#             if sub[j][0] <= l :
#                total+=100
#     mins=max(mins,total)
# print(mins)

# N, L, K = map(int, input().split())

# easy, hard = 0,0
# for i in range(N):
#     sub1, sub2 = map(int, input().split())
#     if sub2 <= L:
#         hard += 1
#     elif sub1 <= L:
#         easy += 1

# ans = min(hard, K) * 140

# if hard < K:
#     ans += min(K-hard, easy) * 100
# print(ans)
        

n,l,k=map(int,input().split())
e=0
h=0
for i in range(n):
    sub1,sub2=map(int,input().split())
    if sub2<=l:
        h+=1
    elif sub1<=l:
        e+=1
res=min(k,h)*140
if h<k:
    res+=min(k-h,e)*100
print(res)