from astar_algo import printboard

def vis_init_r(n,num):
    board=[]
    file = open("arrays%a/arrays%sansR.txt" %(n,num),"r")
    
    message = file.readline()
    for j in range(104):
        file.readline()

    for i in range(n):
        line = file.readline()
        board.append(list(line[:-1]))
    file.close()

    return board,n,num,message

def vis_init_r_b(n,num):
    board=[]
    file = open("arrays%a/arrays%sRbackwards.txt" %(n,num),"r")
    
    message = file.readline()
    for j in range(104):
        file.readline()

    for i in range(n):
        line = file.readline()
        board.append(list(line[:-1]))
    file.close()

    return board,n,num,message

def vis_init_s(n,num):
    board=[]

    file = open("arrays%a/arrays%s.txt" %(n,num),"r")
    for i in range(n):
        line = file.readline()
        board.append(list(line[:-1]))
    file.close()

    return board,n,num

def visualize(board, n, num, message = None, type = 0):
    for i in range(n):
        for j in range(n):
            letter = board[i][j]
            swap = '+'
            if letter == 'O':
                swap = '*'
            elif letter == 'B':
                swap = 'x'
            elif letter == 'X':
                swap = ' '
            elif letter == 'U':
                swap = '-'
            elif letter == 'S':
                swap = 'S'
            elif letter == 'T':
                swap = 'T'
            board[i][j] = swap
    if type == 1:
        f = open("Visualized/arrays%sboard.txt" %(num), "w")
    elif type == 2:
        f = open("Visualized/arrays%srep_astar.txt" %(num),"w")
        f.write(message)
    elif type == 3:
        f = open("Visualized/arrays%sbac_rep_astar.txt" %(num),"w")
        f.write(message)
    elif type == 4:
        f = open("Visualized/arrays%sbackwards.txt" %(num), "w")
    else:
        print('No Type Input')

    printboard(board, n, f)
    f.close()

def main():
    for i in range(50):
        [board,n,num] = vis_init_s(101,i)
        visualize(board, n, num, type = 1)

        [board,n,num,message] = vis_init_r(101,i)
        visualize(board, n, num, message, type = 2)

        [board,n,num,message] = vis_init_r_b(101,i)
        visualize(board, n, num, message, type = 3)
main() 
