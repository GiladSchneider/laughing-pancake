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

def vis_init_s(n,num):
    board=[]

    file = open("arrays%a/arrays%s.txt" %(n,num),"r")
    for i in range(n):
        line = file.readline()
        board.append(list(line[:-1]))
    file.close()

    return board,n,num

def visualize(board, n, num, message = None):
    for i in range(n):
        for j in range(n):
            letter = board[i][j]
            swap = '🟢'
            if letter == 'O':
                swap = '⚪️'
            elif letter == 'B':
                swap = '🟤'
            elif letter == 'X':
                swap = '🔵'
            elif letter == 'U':
                swap = '⚫️'
            elif letter == 'S':
                swap = '😘'
            elif letter == 'T':
                swap = '😵'
            board[i][j] = swap
    if message != None:
        f = open("Visualized/arrays%srepeated_astar.txt" %(num),"w")
        f.write(message)
    else:
        f = open("Visualized/arrays%sboard.txt" %(num), "w")
    printboard(board, n, f)
    f.close()

def main():
    for i in range(50):
        [board,n,num] = vis_init_s(101,i)
        visualize(board, n, num)

        [board,n,num,message] = vis_init_r(101,i)
        visualize(board, n, num, message)
main() 
