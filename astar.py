from os import X_OK
import copy
def insert(address, tree,dict,g):
    tree.append(address)
    
    return siftup(tree,len(tree)-1,dict,g)
    #return tree
def siftup(tree,i,dict,g):
    while i>0:
        if dict[tree[i]]<dict[tree[i//2]] or (dict[tree[i]]==dict[tree[i//2]] and g[tree[i//2]]<g[tree[i]]):
            temp = tree[i//2]
            tree[i//2] = tree[i]
            tree[i] = temp
        i=i//2
    return tree
def pop(tree,dict,g):
    temp = tree[0]
    tree[0] = tree[len(tree)-1]
    del(tree[len(tree)-1])
    return temp,siftdown(tree,dict,g)
def siftdown(tree,dict,g):
    i=0
    while i*2<len(tree):
        sc = smallestchild(i,tree,dict,g)
        if dict[tree[i]]>dict[tree[sc]] or (dict[tree[i]]==dict[tree[sc]] and g[tree[i]]<g[tree[sc]]):
            temp = tree[sc]
            tree[sc] = tree[i]
            tree[i] = temp
            i=sc
        else:
             return tree
    return tree
def smallestchild(i,tree,dict,g):
    if i*2+1==len(tree):
        return i*2
    else:
        if(dict[tree[i*2+1]]>dict[tree[i*2]] or (dict[tree[i*2+1]]==dict[tree[i*2]] and g[tree[i*2+1]]<g[tree[i*2]])):
            return i*2
        else:
            return i*2+1
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
    openhead  = [s]
    closedf=dict()
    parent={s:s}
    #print("%s %s %s %s" %(xstart,ystart,xtar,ytar))
    while(len(openf)>0):
        #printboard(board,n,f)
        counter = counter+1
        [s,openhead] =pop(openhead,openf,g)
        closedf[s] = openf[s]
        del openf[s]
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
        boolean = True
        for a in list:
            if(a in openhead):
             #   if(g[a]<=prev+1):
              #      boolean = False
               #      continue
               # else:
                #    g[a]=prev+1
                    continue
            elif(a in closedf):
           #    if(g[a]<=prev+1):
                   continue
           #     openf[a]=closedf[a]
           #     del closedf[a]
           # else:
           #     openf[a]=h(a,xtar,ytar,n)
          #  print("%s %s" %(prev+1,h(a,xtar,ytar,n)))
            
            g[a] = prev+1
            openf[a]=h(a,xtar,ytar,n)+prev+1
            insert(a,openhead,openf,g)
            parent[a] = s
        
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
        #i=28
        [board,xstart,ystart,xtar,ytar,n,num] =init(101,i)
        loop(board,xstart,ystart,xtar,ytar,n,num)
main()