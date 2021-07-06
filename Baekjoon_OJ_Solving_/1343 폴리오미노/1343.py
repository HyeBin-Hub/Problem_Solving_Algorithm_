

ex = input()
ex = ex.replace("XXXX","AAAA").replace("XX","BB")
result=""
if "X" in ex:
    result = "-1"
else:
    result = ex
print(result)
