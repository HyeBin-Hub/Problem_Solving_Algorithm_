# 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
# 단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.

# 4단계 다시 고치기

import re
def solution(new_id):
    # 1
    new_id=new_id.lower()
    # 2
    new=""
    for i in new_id:
        if i.isalnum():
            new+=i
        elif i in ("-","_","."):
            new+=i

    new_id=new

    # 3
    while ".." in new_id:
        new_id=new_id.replace("..",".")
    # 4 
    if new_id[0]==".":
        new_id=new_id[1:]
    if new_id[-1]==".":
        new_id=new_id[:-1]

    # 5
    if not new_id:
        new_id+="a"
    
    # 6
    if len(new_id)>=16:
        new_id=new_id[:15]
    
    # 7
    if len(new_id)<=2:
        while len(new_id)!=3:
            new_id+=new_id[-1]
    
    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))

