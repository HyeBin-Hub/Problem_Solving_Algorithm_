

"""
a=int(input(),16)
b=hex(a)[2].upper()
for i in range(1,16):
    c=hex(a*i)[2:].upper()
    d=hex(i)[2:].upper()
    print(b+"*"+d+"="+c)
"""

"""
a = input()

for i in range(1, 16):
    result = '{0:x}'.format(int(a, 16) * i)
    print(a + '*' + '{0:x}'.format(i).upper() + '=' + result.upper())
"""

a=int(input(),16) #  2,8,16 => 10
b=hex(a)[2].upper()
for i in range(1,16):
    c=hex(a*i)[2:].upper()
    d=hex(i)[2:].upper()
    print(b+"*"+d+"="+c)
    
