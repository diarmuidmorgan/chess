from gamestring import MO as mov
from gs import gamestate
from models import forest as fort
from stats import analyze as an

#starting to build an interactive game in this file here

board = [[5,3,4,1000,9,4,3,5],
[1,1,1,1,1,1,1,1],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[-1,-1,-1,-1,-1,-1,-1,-1],
[-5,-3,-4,-1000,-9,-4,-3,-5],]

color=1
ep={-1:[], 1:[]}
array=[]
move=0

g=gamestate(board, ep ,[],[])
g.getPinnedSquares()
g.pinPieces()
g.getAllMoves()
g.representBoard()
m=str(input('enter a move:'))
print(m)
m=mov(move)
board=g.moveToInstruction(new_move,color)
g=gamestate(board, ep ,[],[])
g.getPinnedSquares()
g.pinPieces()
g.getAllMoves()
g.representBoard()
