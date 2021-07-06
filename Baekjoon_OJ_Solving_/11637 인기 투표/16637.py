import sys
from collections import Counter
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input()) 
    vote=[int(input())for _ in range(n)]
    total_vote=sum(vote)//2
    max_voter=max(list(Counter(vote).items()))
    if max_voter[1]>1:
        print("no winner")
    elif max_voter[0]>total_vote:
        print("majority winner {}".format(vote.index(max_voter[0])+1))
    else:
        print("minority winner {}".format(vote.index(max_voter[0])+1))