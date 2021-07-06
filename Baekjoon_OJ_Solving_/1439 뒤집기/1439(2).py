t = 0
a = '?'
s = input()
for i in s:
    if i != a: 
        t += 1
    a = i

print(t//2)