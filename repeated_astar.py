from astar_algo import loop

def state_to_xy(state, n):
    return state//(n), state%(n)

def xy_to_state(state_x, state_y, n):
    return (state_x*n)+state_y

def reveal(state_x, state_y, game_board, board, n):
    if state_x > 0:
        game_board[state_x-1][state_y] = board[state_x-1][state_y]
    if state_x < (n-1):
       game_board[state_x+1][state_y] = board[state_x+1][state_y]
    if state_y > 0:
        game_board[state_x][state_y-1] = board[state_x][state_y-1]
    if state_y < (n-1):
        game_board[state_x][state_y+1] = board[state_x-1][state_y]+1

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
        for s in reversed(path):
            to_x, to_y = state_to_xy(path[s], n)
            
            if game_board[to_x][to_y] == 'T':
                game_board[to_x][to_y] = 'X'
                print("Success!")
                found = True
                break

            
            elif game_board[to_x][to_y] == 'B':
                path = loop(game_board, state_x, state_y, xtar, ytar, n, num)
                break

            else:
                state_x, state_y = to_x, to_y
                game_board[state_x][state_y] = 'X'
                reveal(state_x, state_y, game_board, board, n)
    
    return game_board

