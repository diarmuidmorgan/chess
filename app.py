from flask import render_template
from app import app
import time
from flask import request
import json
import gs
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


#idea is to provide a visual interface with chess.js
@app.route('/')
def index():
    '''loads index page'''
    html = open('app/index.html')
    return html

@app.route('/move')
def move():
    global gamestate
    FENstring = args.get('FEN')
    newState = FENtoGS(FENstring)
    



def FENtoGS(FENstring):

    arr = FENstring.split('/')
