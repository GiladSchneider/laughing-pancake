from astar_algo import loop

def b_astar(board,xstart,ystart,xtar,ytar,n,num):
    rev_answer = loop(board,xtar,ytar,xstart,ystart,n,num)
    return reversed(rev_answer)