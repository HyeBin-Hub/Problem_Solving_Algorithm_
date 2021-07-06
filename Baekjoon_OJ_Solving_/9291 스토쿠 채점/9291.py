t=int(input())
for i in range(1,t+1):
    arr=[list(map(int,input().split()))for _ in range(9)]

    
    flag=1

    check_list=[1,2,3,4,5,6,7,8,9]

    # 행 검사
    for row in arr:
        if sorted(row) !=check_list:
            flag=0 # 틀리다
            break

    # 열 검사
    for row in range(9):
        res=[]
        for col in range(9):
            res.append(arr[row][col])
        if sorted(res)!=check_list:
            flag=0
            break
    
    # 3*3 검사
    for row in range(0,9,3):
        for col in range(0,9,3):
            res=[]
            for nrow in range(row,row+3):
                for ncol in range(col,col+3):
                    res.append(arr[nrow][ncol])
            if sorted(res)!=check_list:
                flag=0
                break
        if flag==0:
            break
    if flag==0:
        print("Case {}: INCORRECT".format(i))
    else:
        print("Case {}: CORRECT".format(i))

    input()


    











































# T = int(input())
# chk_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for test_case_no in range(1, T + 1):
#     board = [list(map(int, input().split())) for _ in range(9)]

#     chk1 = 1
#     chk2 = 1
#     chk3 = 1

#     for i in range(9):
#         if sorted(board[i]) != chk_list:
#             chk1 = 0

#     for j in range(9):
#         save_list = []
        
#         for i in range(9):
#             save_list.append(board[i][j])
        
#         if sorted(save_list) != chk_list:
#             chk2 = 0

#     for start_row in range(0, 9, 3):
#         for start_col in range(0, 9, 3):
#             save_list = []

#             for row in range(start_row, start_row + 3):
#                 for col in range(start_col, start_col + 3):
#                     save_list.append(board[row][col])
            
#             if sorted(save_list) != chk_list:
#                 chk3 = 0

#     print('Case {}: '.format(test_case_no), end='')

#     if chk1 + chk2 + chk3 != 3:
#         print('INCORRECT')

#     else:
#         print('CORRECT')

#     r_input()