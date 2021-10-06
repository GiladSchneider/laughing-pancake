from os import X_OK
import copy

def h(s,xtar,ytar,n):
    x= s//n
    y=s%n
    return abs(xtar-x)+abs(ytar-y)

def printboard(board,x,f):
   # f = open("arrays%a/arrays%sans.txt" %(folder,num),"a")
    for i in range(x):
        for j in range(x):
            f.write(board[i][j])
            
        f.write("\n")
    f.write("\n")    
   # f.close()   
    
            
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
def loop(board,xstart,ystart,xtar,ytar,n,num):
    counter=0
    orig = copy.deepcopy(board)
    prev =0
    s = xstart*n+ystart
    x=s//(n)
    y=s%(n)
    g={s:prev}
    f = h(s,xtar,ytar,n)+g[s]
    openf = {s:f}
    closedf=dict()
    parent={s:s}
    #print("%s %s %s %s" %(xstart,ystart,xtar,ytar))
    while(len(openf)>0):
        #printboard(board,n,f)
        counter = counter+1
        s=min(openf, key=openf.get)
        prev =g[s]
         
        x=s//(n)
        y=s%(n)
        board[x][y]='X'
        if(x==xtar and y==ytar):
            break
        #printboard(board,n,f)
        list =[]
        if(x>0 and board[x-1][y]!='B'):
            list.append((x-1)*(n)+y)
        if(x<n-1 and board[x+1][y]!='B'):
            list.append((x+1)*(n)+y)
        if(y>0 and board[x][y-1]!='B'):
            list.append((x)*(n)+y-1)
        if(y<n-1 and board[x][y+1]!='B'):
            list.append((x)*(n)+y+1)
        for a in list:
            if(a in openf):
                if(g[a]<=prev+1):
                     continue
            elif(a in closedf):
           #    if(g[a]<=prev+1):
                   continue
           #     openf[a]=closedf[a]
           #     del closedf[a]
           # else:
           #     openf[a]=h(a,xtar,ytar,n)
            openf[a]=h(a,xtar,ytar,n)+prev+1
            g[a] = prev+1
            parent[a] = s
        closedf[s] = openf[s]
        del openf[s]
    if((x!=xtar or y!=ytar)):
        f = open("arrays%a/arrays%sans.txt" %(n,num),"w")
        f.write("No path found"+"\n")
        printboard(board,n,f)
        f.close
    else:
        f = open("arrays%a/arrays%sans.txt" %(n,num),"w")  
        f.write("board "+str(num)+" Original"+"\n")
        
        printboard(orig,n,f)
        f.write("board "+str(num)+" searched"+"\n")
        printboard(board,n,f)
        coun =0
        start = xstart*n+ystart
        s = xtar*n+ytar
        ans={s:s}
        f.write("board "+str(num)+" Path"+"\n")
        
        while s!=start:     
             ans[coun]= parent[s]
             coun=coun+1
             s= parent[s]
        for s in reversed(ans):
             x=ans[s]//n 
             y=ans[s]%n 
             f.write("(" +str(y+1)+" , "+ str(x+1)+ " )" +"\n")
             orig[x][y] = 'X'
        printboard(orig,n,f)
        f.close

    
def main():
    for i in range(50):
        [board,xstart,ystart,xtar,ytar,n,num] =init(101,i)
        loop(board,xstart,ystart,xtar,ytar,n,num)
main()