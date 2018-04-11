## should search to a certain depth, only considering positions that pass a certain evaluation threshold

def simpleSearch(gameState, color, reject_threshold, killer_threshold, depth=0):
    #doesn't build any kind of tree
    arr=[]
    for move in gameState.getAllMoves():
        #create a newState for every available move - this will be 20 for the first move, growing significantly after that
        newState = gameState.makeNewState(move)

        if newState.evaluate() > threshold:

            gameobject=simpleSearch(newState, color*-1, threshold, depth=depth+1)
            if gameobject.score > threshold:

                arr.append(gameobject)

                if gameobject.score > killer_threshold:
                    #if the score passes a certain killer threshold, just cut the process and return this move
                    return gameobject


    for obj in arr:

        return best_game_object
