import sys

upper = [chr(i) for i in range(65,91)]
lower = [chr(i) for i in range(97,123)]

s = sys.stdin.readline()

t=""

for i in range(len(s)):
    if s[i] in upper:
        t+= chr(ord(s[i])+32)
    if s[i] in lower:
        t+= chr(ord(s[i])-32)
print(*t.split())


# print(ord("a"))
# print(ord("A"))
# print(ord("z"))
# print(ord("Z"))
# print("W",ord("W"))
# print("w",ord("w"))