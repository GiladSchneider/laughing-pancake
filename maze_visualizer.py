from astar_algo import printboard

def vis_init(n,num):
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

def visualize(board, n, num, message):
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
    
    f = open("Visualized/arrays%svis.txt" %(num),"w")
    f.write(message)
    printboard(board, n, f)
    f.close()

def main():
    for i in range(50):
        [board,n,num,message] = vis_init(101,i) #i was using 7x7 arrays to test this chagne the 7 to whatever array size you are using
        visualize(board, n, num, message)
main() 