from flask import render_template
from app import app
import time
from flask import request
import json
import gs
import think
board = [[5,3,4,1000,9,4,3,5],
[1,1,1,1,1,1,1,1],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[-1,-1,-1,-1,-1,-1,-1,-1],
[-5,-3,-4,-1000,-9,-4,-3,-5],]
ep={-1:[], 1:[]}
canCastle = {1000:{'queen':True, 'king':True}, -1000:{'queen':True, 'king':True}}
hasCastled = {1000:False, -1000:False}
gamestate = gs.gamestate(board, ep, canCastle, hasCastled)
from flask import request
import json

#idea is to provide a visual interface with chess.js
@app.route('/')
def index():
    '''loads index page'''
    html = open('app/board.html','r').read()
    return html

@app.route('/move')
def move():
    global gamestate
    FENstring = request.args.get('FEN')
    gamestate = FENtoGS(FENstring, gamestate.board, 1, gamestate.hasCastled, gamestate.canCastle)
    print(gamestate.board)
    return json.dumps({'fen':gsToFen(gamestate)})
def gsToFen(gs):

    board=gs.board
    keys={-5:'r', 5:'R',-1000:'k', 1000:'K', -9:'q',9:'Q',-1:'p', 1:'P', -4:'b', 4:'B', -3:'n', 3:'n'}
    FENstring=''
    for x in range (7, -1, -1):

        numbers=False
        for y in range(0, 8):
            currentNumber=0
            if board[x][y] in keys:
                if not numbers:
                    FENstring+=keys[board[x][y]]
                else:
                    numbers=False
                    FENstring+=str(currentNumber)
                    currentNumber=0
            else:
                currentNumber+=1

        FENstring+='/'

    return FENstring[:-1]




def FENtoGS(FENstring, oldBoard, color, hasCastled, canCastle):
    new_board = [[0 for x in range(8)] for y in range(8)]
    print(new_board)
    keys={'r':-5, 'R':5, 'k':-1000, 'K':1000, 'q':-9, 'Q':9, 'p':-1, 'P':1, 'b':-4, 'B':4, 'n':-3, 'N':3}
    arr = FENstring.split('/')
    print(arr)
    ep={-1:[], 1:[]}
    for x in range(7, -1, -1):

        count=0
        for y in range(0, len(arr[x])):

            if arr[x][y] in keys:
                new_board[7-x][count]=keys[arr[x][y]]
                count+=1
            else:
                count+=int(arr[x][y])


    #compare boards
    differences = []
    for x in range(8):

        for y in range(8):

            if board[x][y]!=new_board[x][y]:

                differences.append({'pos':[x,y], 'newValue':new_board[x][y], 'oldValue':board[x][y]})

    if len(differences) == 2:

        for difference in differences:
            if difference['newValue']==0:
                d1=difference
            else:
                d2=difference
        if color==1 and d2['newValue']==1:
            if d1['pos'][0]==1 and d2['pos'][0]==3:
                ep[1].append(d2['pos'])
        elif color==-1 and d2['newValue']==-1:
            if d1['pos'][0]==6 and d2['pos'][0]==4:
                ep[-1].append(d2['pos'])

        elif abs(d2['newValue'])==1000:

            canCastle[color]['queen']=False
            canCastle[color]['king']=False

        elif abs(d1['oldValue']==5):
            piceColor = int(d1['oldValue']/abs(d1['oldValue']))
            if d1['pos'] == [0,0]:
                canCastle[pieceColor]['king']=False

            elif d1['pos'] == [7,7]:
                canCastle[pieceColor]['queen']=False

            elif d2['pos']== [7,0]:
                canCastle[pieceColor]['king']=False

            elif d1['pos']== [0,7]:
                canCastle[pieceColor]['queen']=False



        #just check for enpassants if this is the case

    else:
        for difference in differences:

            if difference['pos']==[0, 4]:
                hasCastled[1]=True
            elif difference['pos']==[7,4]:
                hasCastled[-1]=True


    return gs.gamestate(new_board, ep, canCastle, hasCastled)

        #check for castles
