import random as rnd



size =4

min_skor=0
max_skor =2
total_skor = 0


def new_board():
    board=[[0]*size for _ in range(size)]
    ad_new_board(board)
    ad_new_board(board)
    return board


    
def ad_new_board(board):
    empty = [(r,c)for r in range(size) for c in range(size) if board[r][c] ==0]
    if empty:
        r,c =rnd.choice(empty)
        board[r][c]= rnd.choice([2,2,2,4])
    else:
        print("game over!!")
        return "q"


        

def print_board(board):
    for row in board:
        print(row)
    print()

def compress(row):
    new_row=[num for num in row if num !=0]
    new_row+=[0]* (size-len(new_row))
    return new_row

def merge(row):
    global total_skor
    for i in range(size-1):
        if row[i]!=0 and row[i]==row[i+1]:
            row[i]+=row[i]
            row[i+1]=0
    return row

def move_left(board):
    new_board=[]
    for row in board:
        row=compress(row)
        row=merge(row)
        row=compress(row)
        new_board.append(row)
    return new_board

def move_right(board):
    new_board=[]
    for row in board:
        row=row[::-1]
        row=compress(row)
        row=merge(row)
        row=compress(row)
        row=row[::-1]
        new_board.append(row)
    return new_board

def tersboard(board):
    return [list(row) for row in zip(*board)]

def move_up(board):
    board = tersboard(board)
    board = move_left(board)
    board =tersboard(board)
    return board

def move_down(board):
    board = tersboard(board)
    board = move_right(board)
    board =tersboard(board)
    return board


def baslat(callback=None):
    board = new_board()
    print_board(board)
    while True:
        move = input("Hamle (w=up, s=down, a=left, d=right, q=quit): ")
        if move == 'q' or ad_new_board(board) =="q":
            return callback()
        elif move == 'a':
            board = move_left(board)
        elif move == 'd':
            board = move_right(board)
        elif move == 'w':
            board = move_up(board)
        elif move == 's':
            board = move_down(board)
        else:
            print("Geçersiz hamle!")
            continue

        ad_new_board(board)
        print_board(board)

