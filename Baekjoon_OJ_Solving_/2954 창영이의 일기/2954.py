arr = ['a', 'i', 'e', 'o', 'u']
s = input().rstrip()
for c in arr:
    s = s.replace(c+'p'+c, c)
print(s)
