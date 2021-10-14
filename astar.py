from astar_algo import loop

#initializes the boards
def init(n,num):
    board=[]
    #print ("arrays5/arrays%s.txt" %(num))
    file = open("arrays%a/arrays%s.txt" %(n,num),"r")
    for i in range(n):
        line = file.readline()
        if ('S' in line):
            xstart = i
            ystart = line.index('S'); 
        if ('T' in line):
            xtar = i 
            ytar = line.index('T')
        #print(list(line))
        board.append(list(line[:-1]))
    #printboard(board,n,num,folder)
    return board,xstart,ystart,xtar,ytar,n,num

#Imports the boards from the txt files
def main():
    for i in range(50):
        #i=28
        [board,xstart,ystart,xtar,ytar,n,num] = init(101,i)
        loop(board,xstart,ystart,xtar,ytar,n,num)
main()
