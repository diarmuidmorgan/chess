#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 15:56:22 2018

@author: eoin
"""

import miner
import pandas as pd
games = pd.read_csv('data/cleanChess.csv')
games_exploded = miner.mine(games.iloc[0])

def exploder(x):
    limit = min(500 * x, games.shape[0])
    start = limit - 500
    games_exploded = miner.mine(games.iloc[start])
    for i in range(start+1, limit):
        if ((i-1) % 100 == 0):
            print("Games Exploded:", i, '/', games.shape[0])
        try:
            exploded_game = miner.mine(games.iloc[i])
            games_exploded = games_exploded.append(exploded_game)
        except Exception as e:
            print("Error on game:", i, "Reason:", e)
    games_exploded.to_csv('data/explodedCleanChess' + str(x) + '.csv', index=False)


x = 1
while ((x-1) * 500) < games.shape[0]:
    exploder(x)
    x+=1
