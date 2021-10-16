from astar_algo import loop
from astar_algo import printboard
from astar import init

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
        game_board[state_x][state_y+1] = board[state_x-1][state_y+1]

# Returns game_board on success
def r_astar(board, xstart, ystart, xtar, ytar, n, num):
    #The board that is visible to the agent -- Starts blank
    game_board = [['U']*n for _ in range(n)]
    
    state = xy_to_state(xstart, ystart, n)
    state_x, state_y = state_to_xy(state, n)
    game_board[xstart][ystart] = 'S'
    
    goal_state = xy_to_state(xtar, ytar, n)
    goal_x, goal_y = state_to_xy(goal_state, n)
    game_board[goal_x][goal_y] = 'T'

    #Initial Drop of Agent into field reveles the squares around the agent
    reveal(xstart, ystart, game_board=game_board, board=board, n=n)
    
    #Start the game loop
    path = loop(game_board, xstart, ystart, xtar, ytar, n, num)
    
    found = False
    while not found:

        # If no path exists, stop
        if path == None:
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

        for s in reversed(path):
            # Reveal current location and calculate next move
            reveal(state_x, state_y, game_board, board, n)
            to_x, to_y = state_to_xy(path[s], n)
            
            # If the path starts w the current position, continue to next move
            if to_x == state_x and to_y == state_y:
                    continue
            
            # If your next move is obstructed, recalculate the path
            if game_board[to_x][to_y] == 'B':
                path = loop(game_board, state_x, state_y, xtar, ytar, n, num)
                break
            
            # If your path is not obstructed, take a step
            else:
                state_x, state_y = to_x, to_y
                
                # Check for a win
                if state_x == goal_x and state_y == goal_y:
                    print("Success!")
                    found = True
                    break
                else:
                    game_board[state_x][state_y] = 'X'
                
                
                
    
    f = open("arrays%a/arrays%sansR.txt" %(n,num),"w")
    f.write("Path found"+"\n")
    f.write("board "+str(num)+" Original"+"\n")
    printboard(board,n,f)
    f.write("board "+str(num)+" searched"+"\n")
    printboard(game_board,n,f)
    f.close()
    return game_board

for i in range(50):
        [board,xstart,ystart,xtar,ytar,n,num] = init(101,i) #i was using 7x7 arrays to test this chagne the 7 to whatever array size you are using
        r_astar(board,xstart,ystart,xtar,ytar,n,num)
