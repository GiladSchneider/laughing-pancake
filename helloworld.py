import random
#def iter(board,n):
#    for i in range(n):
#        for j in range(n):
#            if((board[i][j])=='U'):
#                board[i][j]=block()
#    return board
def printboard(board,x,num):
   # for i in range(x):
    #    for j in range(x):
     #       print("%s " % (board[i][j]), end="",flush=True)
            
      #  print()
    #print()    
    f = open("arrays%s/arrays%s.txt" %(x,num),"w")
    for i in range(x):
        for j in range(x):
            f.write(board[i][j])
            
        f.write("\n")
    f.write("\n")    
    f.close()
def block():
     
    if random.randint(0, 10)>6:
        return 'B'
    else:
        return 'O'

def creator(board,n,mystack):
    #print(mystack)
    while True:
        temp = mystack.pop()
        #print(temp)
        x= temp//(n)
        y = temp%(n)
    # printboard(board,n)
        if(board[x][y]=='U'):
            
                    board[x][y]='O'
        list =[]
        if(x>0 and board[x-1][y]=='U'):
            list.append((x-1)*(n)+y)
        if(x<n-1 and board[x+1][y]=='U'):
            list.append((x+1)*(n)+y)
        if(y>0 and board[x][y-1]=='U'):
            list.append((x)*(n)+y-1)
        if(y<n-1 and board[x][y+1]=='U'):
            list.append((x)*(n)+y+1)
        #print(list)
        if(len(list)==0):
            if(len(mystack)==0):
            #  print(mystack)
                #printboard(board,n)
            
                return board
           
                
        else:
            dir = random.randint(0, len(list)-1)
            xnew = list[dir]//(n) 
            ynew = list[dir]%(n)
            #print("%s %s" %(xnew,ynew))
            result = block()
            board[xnew][ynew] = result
            mystack.append(x*(n)+y)
            if(result=='O'):
                mystack.append(xnew*n+ynew)
                
                
            
            
        
            
def check(board,n):
    for i in range(n):
        for j in range(n):
           
            if(board[i][j]=='U'):
                #print("%s %s" %(i,j))
                return i*n+j
    return -1 
def main(n):
    
    for num in range (50):
        board = [['U']*n for _ in range(n) ]
        xstart = random.randint(0, n-1)
        ystart = random.randint(0, n-1)
        xtar = xstart
        ytar = ystart
        #print("%s %s" % (xstart,ystart))
        board[xstart][ystart] = 'S'
        while xtar==xstart and ytar == ystart:
            xtar = random.randint(0, n-1)
            ytar = random.randint(0, n-1)

        board[xtar][ytar] = 'T'
        stack =[]
        #print("%s %s %s %s" % (xstart,ystart,xtar,ytar))
        stack.append(xstart*(n)+ystart)
        #hi = creator(board,n,stack)
        #printboard(board,n)
        #temp = check(board,n)+1
    # while temp !=-1:
        #   stack.append(temp)
        #  creator(board,n,stack)
        #  temp = -1
        # temp = check(board,n)
        hi = creator(board,n,stack)
        temp = check(board,n)
        while temp !=-1:
            stack.append(temp)
            creator(board,n,stack)
            temp = -1
            temp = check(board,n)
        #iter(board,n)
        printboard(board,n,num)

main(101)



