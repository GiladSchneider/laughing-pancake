# set key value pair hue. after fisrt run through, go to parent, and set counter as 0.
#  go through the correct path ad give each a heu value of counter until hit start 
#go through rest of parent, and if node n not already in heu, go back up the tree x amount of times until find 
#something that already in heu (node m), and give node m a heu value of x+heu(n).
# then when setting openf in loop, say if(s is in heu): k = heu(s) else k=h(s,xtar,ytar,n)
#point is will have a bunch of different starting points over multiple runs, but 1 target thats constant.
#also, even if already in heu, can replace value with smaller number     quick psuedocode for adaptive. will try to code saturday night i guess when repeated a star is done
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
def loop(board,xstart,ystart,xtar,ytar,n,num,hue):
    
    counter=0
    orig = copy.deepcopy(board)
    prev =0
    s = xstart*n+ystart
    x=s//(n)
    y=s%(n)
    g={s:prev}
    if(s in hue):
        f = hue[s]+g[s]
    else:
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
       # boolean = True
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
            if(a in hue):
                openf[a]= hue[a]+g[a]
            else:
                openf[a]= h(a,xtar,ytar,n)+g[a]
            insert(a,openhead,openf,g)
            parent[a] = s
        
    if((x!=xtar or y!=ytar)):
        a= dict()
        b = dict()
        return a,hue,b
      #  f = open("arrays%a/arrays%sans.txt" %(n,num),"w")
       # f.write("No path found"+"\n")
        #printboard(board,n,f)
      #  f.close
    else:
       # f = open("arrays%a/arrays%sans.txt" %(n,num),"w")  
       # f.write("board "+str(num)+" Original"+"\n")
        
       # printboard(orig,n,f)
        #f.write("board "+str(num)+" searched"+"\n")
       # printboard(board,n,f)
        coun =1
        start = xstart*n+ystart
        s = xtar*n+ytar
        ans={0:s}
       # f.write("board "+str(num)+" Path"+"\n")
        
        while s!=start:     
             ans[coun]= parent[s]
             coun=coun+1
             s= parent[s]
        #for s in reversed(ans):
        #     x=ans[s]//n 
         #    y=ans[s]%n 
         #    f.write("(" +str(y+1)+" , "+ str(x+1)+ " )" +"\n")
         #    orig[x][y] = 'X'
       # printboard(orig,n,f)
       # f.close
        return ans,hue,parent
    
def state_to_xy(state, n):
    return state//(n), state%(n)

def xy_to_state(state_x, state_y, n):
    return (state_x*n)+state_y

def reveal(state_x, state_y, game_board, board, n):
    if (state_x > 0) and (game_board[state_x-1][state_y] != 'X'):
        game_board[state_x-1][state_y] = board[state_x-1][state_y]
    
    if (state_x < (n-1)) and (game_board[state_x+1][state_y] != 'X'):
       game_board[state_x+1][state_y] = board[state_x+1][state_y]
    
    if (state_y > 0) and (game_board[state_x][state_y-1] != 'X'):
        game_board[state_x][state_y-1] = board[state_x][state_y-1]
    
    if (state_y < (n-1)) and (game_board[state_x][state_y+1] != 'X'):
        game_board[state_x][state_y+1] = board[state_x][state_y+1]

# Returns game_board on success
def r_astar(board, xstart, ystart, xtar, ytar, n, num):
    # The board that is visible to the agent -- Starts blank
    game_board = [['U']*n for _ in range(n)]
    
    state = xy_to_state(xstart, ystart, n)
    state_x, state_y = state_to_xy(state, n)
    game_board[xstart][ystart] = 'S'
    
    goal_state = xy_to_state(xtar, ytar, n)
    goal_x, goal_y = state_to_xy(goal_state, n)
    game_board[goal_x][goal_y] = 'T'

    # Initial Drop of Agent into field reveles the squares around the agent
    reveal(xstart, ystart, game_board=game_board, board=board, n=n)
    hue = dict()
    #Start the game loop
    path,hue,parent = loop(copy.deepcopy(game_board), state_x, state_y, goal_x, goal_y, n, num,hue)
    found = False
    while not found:

        # If no path exists, stop
        if path == None or len(path)==0:
            game_board[xstart][ystart], game_board[goal_x][goal_y] = 'S', 'T'
            f = open("arrays%a/arrays%sansR.txt" %(n,num),"w")
            f.write("No path found"+"\n")
            f.write("board "+str(num)+" Original"+"\n")
            printboard(board,n,f)
            f.write("board "+str(num)+" searched"+"\n")
            printboard(game_board,n,f)
            f.close()
            print('No Path Available')
            found = True
            return game_board

        counter =0
    
        for s in list(range(len(path))):
            hue[path[s]]=counter
            counter+=1
        for p in parent:
            
            counter =0
            b=p
            while not(b in hue):
                b = parent[b]
                counter+=1
            if not(p in hue) or hue[p]<hue[b]+counter:
                hue[p] = hue[b]+counter
        for s in reversed(list(range(len(path)))):
            # Reveal current location and calculate next move
            reveal(state_x, state_y, game_board, board, n)
            to_x, to_y = state_to_xy(path[s], n)
            # if to_x == state_x and to_y == state_y:
            #     print('ERR 1')
            #     continue

            # If your next move is obstructed, recalculate the path
            if board[to_x][to_y] == 'B':
                #print('ERR 2')
                path,hue,parent = loop(copy.deepcopy(game_board), state_x, state_y, xtar, ytar, n, num,hue)
                break
            
            # If your path is not obstructed, take a step
            else:
                state_x, state_y = to_x, to_y
                # Check for a win
                if state_x == goal_x and state_y == goal_y:
                    print("Success!")
                    game_board[xstart][ystart], game_board[goal_x][goal_y] = 'S', 'T'
                    found = True
                    break
                else:
                    game_board[state_x][state_y] = 'X'
                    #
            counter+=1
    f = open("arrays%a/arrays%sansR.txt" %(n,num),"w")
    f.write("Path found"+"\n")
    f.write("board "+str(num)+" Original"+"\n")
    printboard(board,n,f)
    f.write("board "+str(num)+" searched"+"\n")
    printboard(game_board,n,f)
    f.close()
    return game_board

for i in range(50):
        [board,xstart,ystart,xtar,ytar,n,num] = init(7,i)
        r_astar(board,xstart,ystart,xtar,ytar,n,num)