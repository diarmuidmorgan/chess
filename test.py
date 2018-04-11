from pieces.vc import validCoords
from pieces import pawn, king, queen, bishop, knight, rook


pieces = {'PAWN':8, 'ROOK': 2, 'KNIGHT':2, 'BISHOP':2, 'KING':1, 'QUEEN':1}
values = {'PAWN':1, 'KNIGHT':3, 'BISHOP':4, 'ROOK':5, 'QUEEN':9, 'KING':1000}


p = pawn.pawn(pieces)
k=king.king(pieces)
r=rook.rook(pieces)
N=knight.knight(pieces)
b=bishop.bishop(pieces)
q=queen.queen(pieces)

board = [[5,3,4,1000,9,4,3,5],
[1,1,1,1,1,1,1,1],
[0,0,0,0,0,0,0,0],
[-4,0,0,-9,0,0,0,0],
[-1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[-1,-1,-1,-1,-1,-1,-1,-1],
[-5,-3,-4,-1000,-9,-4,-3,-5],]

#pins are working now, kind of.
print(k.returnPins(0,3,1,board))
