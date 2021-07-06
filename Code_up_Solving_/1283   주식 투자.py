# 1
a=int(input())  
b=int(input())
s=list(map(int,input().split()))
q=a
for i in range(b):
    if s[i]>0:# 양수
        q=q+(q*(s[i]/100))
    else:
        q=q-(q*(abs(s[i])/100))

if q-a>0:
    print(round(q-a))
    print("good")
elif q-a<0:
    print(round(q-a))
    print("bad")
else:
    print(round(q-a))
    print("same")
    
# 2

a = int(input())
b = int(input())
variabilities = list(map(int, input().split()))
final_money = a
​
for variability in variabilities:
    if variability < 0:
        final_money = final_money - (final_money * (variability * -1 / 100))
    else:
        final_money = final_money + (final_money * (variability / 100))
​
print(round(final_money - a))
if(final_money - a == 0):
    print('same')
elif(final_money - a < 0):
    print('bad')
else:
    print('good')
