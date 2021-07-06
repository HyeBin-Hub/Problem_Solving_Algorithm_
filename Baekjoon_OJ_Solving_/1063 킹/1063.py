king,stone,num=input().rstrip().split()

king_x=abs(int(king[1])-8)
king_y=ord(king[0])-65

stone_x=abs(int(stone[1])-8)
stone_y=ord(stone[0])-65

for _ in range(int(num)):
    s=input().rstrip()

    if s=="R":
        if king_y+1 <8 :
            if (king_x==stone_x and king_y+1==stone_y) :
                if  stone_y+1<8:
                    stone_x+=1
                    king_y+=1
            else:
                king_y+=1

    elif s=="L":
        if 0<=king_y-1 :
            if (king_x==stone_x and king_y-1==stone_y) :
                if 0 <=stone_y-1:
                    stone_y-=1
                    king_y-=1
            else:
                king_y-=1
    
    elif s=="B":
        if king_x+1 <8 :
            if (king_x+1==stone_x and king_y==stone_y) :
                if  stone_x+1<8:
                    stone_x+=1
                    king_x+=1
            else:
                king_x+=1

    elif s=="T":
        if 0<=king_x-1:
            if (king_x-1==stone_x and king_y==stone_y):
                if stone_x-1<8:
                    stone_x-=1
                    king_x-=1
            else:
                king_x-=1

    elif s=="RT":
        if king_x-1 >= 0 and king_y+1 < 8:
            if (king_x-1==stone_x and king_y+1==stone_y):
                if stone_x-1>=0 and stone_y+1<8:
                    stone_x-=1
                    stone_y+=1
                    king_x-=1
                    king_y+=1
            else:
                king_x-=1
                king_y+=1

    elif s=="LT":
        if king_x-1 >= 0 and king_y-1 >=0:
            if (king_x-1==stone_x and king_y-1==stone_y):
                if stone_x-1>=0 and stone_y-1>=0:
                    stone_x-=1
                    stone_x-=1
                    king_x-=1
                    king_y-=1
            else:
                king_x-=1
                king_y-=1

    elif s=="RB":
        if king_x+1 <8 and king_y+1<8:
            if (king_x+1==stone_x and king_y+1==stone_y):
                if stone_x+1<8 and stone_y+1<8:
                    stone_x+=1
                    stone_y+=1
                    king_x+=1
                    king_y+=1
            else:
                king_x+=1
                king_y+=1

    elif s=="LB":
        if king_x+1 <8 and king_y-1 >=0:
            if (king_x+1==stone_x and king_y-1==stone_y):
                if stone_x+1<8 and stone_y-1>=0:
                    stone_x+=1
                    stone_y-=1
                    king_x+=1
                    king_y-=1
            else:
                king_x+=1
                king_y-=1
 
print(chr(king_y+65)+str(8-king_x))
print(chr(stone_y+65)+str(8-stone_x))

